# -*- coding: utf-8 -*-
# @Time :2020/11/23 上午11:48
# @Author   : zhouchengwei
# @File :test_model_zm


from __future__ import print_function
import sys

import os
import cv2
import PIL
import torch
import glob
import time
import argparse
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from os import listdir
from os.path import isdir, isfile, join, abspath



def list_all_files(root):
    files = [join(root, f) for f in listdir(root) if isfile(join(root, f))]
    dirs = [d for d in listdir(root) if isdir(join(root, d))]
    for d in dirs:
        files_in_d = list_all_files(join(root, d))
        if files_in_d:
            for f in files_in_d:
                files.append(join(f))
    return files

def list_all_files_relative(root):
    files = [f for f in listdir(root) if isfile(join(root, f))]
    dirs = [d for d in listdir(root) if isdir(join(root, d))]
    for d in dirs:
        files_in_d = list_all_files(join(root, d))
        if files_in_d:
            for f in files_in_d:
                files.append(f)
    return files

def contours_result_bev(contours, hierachy):
    bev_img = np.zeros((1020, 1920, 3), np.uint8)
    if hierachy is not None:
        for i in range(len(hierachy)):
            is_fs = is_freespace(i, hierachy)
            # print (i)
            # print (contours[i])
            if (len(contours[i]) < 3):
                continue
            cv2.drawContours(bev_img, [np.array(contours[i])], -1, (0, 255, 255) if is_fs else (255, 0, 0), 2)
    return bev_img


def undistort_result_uv(blend_img, contours, hierachy, K, D, new_K):
    und_blend_img = undistort_image(blend_img, K, D, new_K)
    # und_blend_img = blend_img#undistort_image(blend_img, K, D , new_K)
    # print(c.shape)
    if hierachy is not None:
        undistorted_contours = undistort_contours(contours, K, D, new_K)
        # undistorted_contours = contours#undistort_contours( contours , K , D , new_K)
        for i in range(len(hierachy)):
            is_fs = is_freespace(i, hierachy)
            cv2.drawContours(und_blend_img, undistorted_contours, i, (0, 255, 255) if is_fs else (255, 0, 0), 2)
    return und_blend_img


# def OrthProject(points,dim1, dim2, img_size=[1444,1444], world_size= [100,100], world_center = [0,0,0], z_range = [0,2] ):
def project_to_2d(contours, dim1, dim2, img_size=[1020, 1920], world_size=[1020 // 12, 1920 // 12]):
    # gns_threshold = 0.15
    ratio = np.array(world_size, np.float32) / np.array(img_size, np.float32)
    max_ratio = float(np.max(ratio))

    img = np.zeros(img_size, np.uint8)
    img[:, :] = 0

    converted_points_list = []
    converted_points_on_bev_list = []

    for points in contours:
        converted_points = []
        converted_points_on_bev = []
        for pt in points:
            if pt[0] < 80 and pt[0] > 0 and pt[1] > -60 and pt[1] < 60:
                # print (max_ratio, pt)
                pt = np.array(pt)
                # pt += hf_ws
                img[int(950 - (pt[dim1]) / max_ratio),
                    1920 // 2 - int((pt[dim2]) / max_ratio) - 1] = 255

                converted_points.append([pt[dim1], pt[dim2]])  # world
                converted_points_on_bev.append(
                    [1920 // 2 - int((pt[dim2]) / max_ratio) - 1, int(950 - (pt[dim1]) / max_ratio)])  # bev img
        converted_points_list.append(converted_points)
        converted_points_on_bev_list.append(converted_points_on_bev)

    return img, converted_points_list, converted_points_on_bev_list, {'img_size': img_size, 'world_size': world_size,
                                                                      'max_ratio': max_ratio}

def reference_image(img_size=[1020, 1920], ratio=0.1):
    img = np.zeros((1020, 1920, 3), np.uint8)
    img[:, 1920 // 2] = (255, 255, 255)
    img[950, :] = (255, 255, 255)

    img[int(950 - 2.0 / ratio), :] = (255, 0, 255)
    img[int(950 - 4.0 / ratio), :] = (255, 0, 255)
    img[int(950 - 6.0 / ratio), :] = (255, 0, 255)
    img[int(950 - 8.0 / ratio), :] = (255, 0, 255)

    img[int(950 - 10.0 / ratio), :] = (255, 0, 255)
    img[int(950 - 20.0 / ratio), :] = (255, 0, 255)
    img[int(950 - 30.0 / ratio), :] = (255, 0, 255)
    img[int(950 - 40.0 / ratio), :] = (255, 0, 255)
    img[int(950 - 50.0 / ratio), :] = (255, 0, 255)

    car_size = [2.48, 1.815]  # x, y

    y1 = int(950 - (car_size[0] / ratio) / 2)
    x1 = int(1920 // 2 - (car_size[1] / ratio) / 2)

    y2 = int(950 + (car_size[0] / ratio) / 2)
    x2 = int(1920 // 2 + (car_size[1] / ratio) / 2)
    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
    return img  # cmap[img]


def load_ROI_masks(root_dir):
    ROI_masks_cache = {}
    #masks_dir = join(self.root, self.task + '_masks')
    masks_dir = join(root_dir, 'train_masks')
    '''
    dirs = [ d for d in listdir(masks_dir) if isdir(join(masks_dir,d))]
    for d in dirs:
        mask_par_dir = join(masks_dir,d)
        mask_file_path = join(mask_par_dir,'__ROI__.png')
        mask_img = cv2.imread(mask_file_path, cv2.IMREAD_GRAYSCALE)
        self.ROI_masks_cache[mask_par_dir] = mask_img
    '''
    to_find_ROI = list_all_files(masks_dir)
    for f in to_find_ROI:
        if os.path.basename(f) == '__ROI__.png':
            print("Loading ROI mask : " + f)
            mask_img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            ROI_masks_cache[os.path.dirname(f)] = mask_img
    return ROI_masks_cache
# print (self.ROI_masks_cache)


def find_ROI_mask(mask_file_path, ROI_masks_cache):
    # print ("Finding ROI mask for : " +mask_file_path)
    try_path = os.path.dirname(mask_file_path)
    while try_path != '' and try_path != '/':
        # print(try_path)
        if try_path in ROI_masks_cache:
            # print ("Found ROI mask : " +try_path)
            return ROI_masks_cache[try_path].copy()
        try_path = os.path.dirname(try_path)
    # print ("ROI mask not found!")
    return None


def check_dir(obj_dir):
    if not os.path.exists(obj_dir):
        os.makedirs(obj_dir)


def create_label_list(file_path, root_dir):
    labels_list = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            name, weight = line.split('\t')
            if not name.endswith('__ROI__.png'):
                labels_list.append(os.path.join(root_dir, name))
    return labels_list



# ---------------------------------- settings --------------------------------------
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu_id", default=0, help="choose the available gpu.")
    parser.add_argument("--test_dir", default="/data/zm_test/test", help="the images prepare to process.")
    parser.add_argument("--res_dir", default="/data/zm_test/res", help="the dir for results.")
    args = parser.parse_args()
    test_dir = args.test_dir
    save_dir = args.res_dir
    sys.path.append("../project_parking")
    workspace = '/data/projects/holo-segmentation-pytorch'
    sys.path.append(workspace)
    from ipm import *  # extract_contours , is_freespace
    from models.tda4_swiftnet import swiftnet as model
    from utils.helpers import prepare_img
    from metric.iou import IoU
    # -----------------------------------------------------------------------------------

    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu_id)
    dataset_dir = '/data/datasets/left_segmentation_annotation'
    has_cuda = torch.cuda.is_available()
    cmap = np.load(os.path.join(workspace, 'utils/cmap.npy'))
    img_size = (1920, 1020)
    img_size_infer = (1920 // 2, 1020 // 2)

    n_classes = 2
    restore_from = '/data/projects/holo-segmentation-pytorch/experiments/project_parking_combine/models_new4_add_5w/best_resnet18_fpn_cityscapes.pth'


    # init models
    net = model(num_classes=n_classes, pretrained=False)

    print("Load checkpoint from %s" % restore_from)
    if has_cuda:
        net.load_state_dict(torch.load(restore_from), strict=True)
    else:
        net.load_state_dict(torch.load(restore_from, map_location='cpu'))

    net.eval()
    if has_cuda:
        net = net.cuda()

    # run and plot
    n_cols = 2
    # n_rows = len(imgs)
    plt.figure(figsize=(24, 64))
    plt.subplots_adjust(wspace=0.2, hspace=0.2)
    idx = 1
    ###############
    intrinsic_yaml, extrinsic_yaml = load_cam_param()
    K, D, new_K = cam_intrinsic(intrinsic_yaml)
    Pos, Quat, bTc = cam_extrinsic(extrinsic_yaml)
    ###
    check_dir(save_dir)
    images_list = list_all_files_relative(test_dir)
    i = 1
    with torch.no_grad():
        for image_relative in images_list:
            image_path = join(test_dir, image_relative)
            save_path = join(save_dir, image_relative)
            # load image
            filepath, filename = os.path.split(image_path)
            print("processing image: %s, [%d / %d]" % (filename, i, len(images_list)))
            i += 1

            #img_origin = np.array(Image.open(img_path).convert("RGB").resize((1920, 1020), PIL.Image.ANTIALIAS))
            img_origin = np.array(Image.open(image_path).convert("RGB"))
            img_origin = cv2.resize(img_origin, img_size, interpolation=cv2.INTER_LINEAR)
            img_infer = cv2.resize(img_origin, img_size_infer, interpolation=cv2.INTER_LINEAR)

            img_inp = torch.tensor(prepare_img(img_infer).transpose(2, 0, 1)[None]).float()
            if has_cuda:
                img_inp = img_inp.cuda()
            segm = net(img_inp)

            # print("output shape {}".format(segm.shape))

            # plot result
            segm = segm[0].data.cpu().numpy().transpose(1, 2, 0)
            segm = cv2.resize(segm, img_size, interpolation=cv2.INTER_LINEAR)
            segm_resized = segm.argmax(axis=2).astype(np.uint8).copy()
            # print (segm_resized)
            segm = cmap[segm.argmax(axis=2).astype(np.uint8)]

            alpha = 1
            beta = 0.7  # 1-alpha
            gamma = 0
            # print("shapppppppppppp:", np.shape(img_origin))
            blend_img = cv2.addWeighted(img_origin, alpha, segm, beta, gamma)
            #
            # if save_pd_mask:
            #     save_pd_mask_path = img_path.replace("train_images", save_dir + '/' + predict_masks)
            #     os.makedirs(os.path.dirname(save_pd_mask_path), exist_ok=True)
            #     save_pd_mask_path = os.path.splitext(save_pd_mask_path)[0] + '.png'
            #     cv2.imwrite(save_pd_mask_path, segm_resized)

            contours, hierachy = extract_contours(segm_resized)

            und_blend_img = undistort_result_uv(blend_img, contours, hierachy, K, D, new_K)

            IPMed_points = IPM_contours(contours, new_K, bTc)
            if IPMed_points is None:
                print("detected no contours , ignored.")
                continue
            simple_ipm_img, ipm_points_list, converted_points_on_bev_list, des = project_to_2d(IPMed_points, 0, 1)
            ipm_img = contours_result_bev(converted_points_on_bev_list, hierachy)
            ref_img = reference_image(ratio=des['max_ratio'])
            ipm_img = cv2.addWeighted(ipm_img, alpha, ref_img, beta, gamma)

            # converted =  np.zeros(ipm_img.shape,np.float32)
            # for i in range(ipm_img.shape[0]):
            #    for j in  range(ipm_img.shape[1]):
            #        converted[i][j] = ipm_img[ipm_img.shape[0] -i -1][j]

            und_blend_img = np.concatenate((und_blend_img, ipm_img), axis=1)

            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            debug_img = Image.fromarray(und_blend_img.astype(np.uint8), mode='RGB')

            print(save_path)
            debug_img.save(save_path)