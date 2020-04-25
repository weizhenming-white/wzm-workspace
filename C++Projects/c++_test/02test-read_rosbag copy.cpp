// 02test-read_rosbag.cpp -- read rosbag and save as txt

rosbag::Bag bag;
bag.open("2020-04-23-10-47-52_rear_1.bag", rosbag::bagmode::Read);
 
std::vector<std::string> topics;
topics.push_back(std::string("chatter"));
topics.push_back(std::string("numbers"));
 
rosbag::View view(bag, rosbag::TopicQuery(topics));//note:TopicQuery;TypeQuery
	
//   std::vector<std::string> types;
//   types.push_back(std::string("geometry_msgs/TransformStamped"));
//   rosbag::View view(bag, rosbag::TypeQuery(types));
 
foreach(rosbag::MessageInstance const m, view)
{
    std_msgs::String::ConstPtr s = m.instantiate<std_msgs::String>();
    if (s != NULL)
        ASSERT_EQ(s->data, std::string("foo"));
 
    std_msgs::Int32::ConstPtr i = m.instantiate<std_msgs::Int32>();
    if (i != NULL)
        ASSERT_EQ(i->data, 42);
}
 
bag.close();
