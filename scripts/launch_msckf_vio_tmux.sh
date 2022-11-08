# Launch msckf nodes and an rviz
cd ~/catkin_ws
tmux new-session -s msckf \; \
  send-keys 'source devel/setup.bash' C-m \; \
  send-keys 'roslaunch msckf_vio msckf_vio_cmu.launch' C-m \; \
  split-window -v \; \
  send-keys 'source devel/setup.bash' C-m \; \
  send-keys 'rviz -d src/msckf_vio/rviz/rviz_cmu_config.rviz' C-m \; \
  split-window -h \; \
  send-keys 'cd ~/data' C-m \; \
  select-pane -t 0 \; \
  split-window -h \; \
  send-keys 'cd ~/data' C-m \; \
