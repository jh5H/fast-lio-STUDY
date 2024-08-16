
```bash
sudo apt-get install libqt5serialport5-dev
```

<br/>
<br/>


```bash
mkdir -p ros2_ws/src
cd ros2_ws/src
git clone -b ros2 --recursive https://github.com/ElettraSciComp/witmotion_IMU_ros.git witmotion_ros
cd ros2_ws
colcon build --packages-select witmotion_ros
source install/setup.bash
```

<br/>
<br/>


```bash

./create_udev_rules.sh
```

<br/>
<br/>

 > wt901_launch.py 파일을 바꿔줍니다.

<br/>

 > wt901.yml 파일을 바꿔줍니다.

<br/>
<br/>
<br/>
<br/>

```bash
ros2 launch witmotion_ros wt901_launch.py
```

