
[witmotion_ros 패키지 설치]  


```bash
sudo apt-get install libqt5serialport5-dev
```

<br/>
<br/>
<br/>


```bash
mkdir -p ros2_ws/src
cd ~/ros2_ws/src
git clone -b ros2 --recursive https://github.com/ElettraSciComp/witmotion_IMU_ros.git witmotion_ros
cd ~/ros2_ws
colcon build --packages-select witmotion_ros
source install/setup.bash
```

<br/>
<br/>
<br/>


[fast-lio-STUDY 자료 설치]  

```bash
cd ~
git clone https://github.com/jh5H/fast-lio-STUDY.git
```
<br/>
<br/>
<br/>

 > wt901_launch.py, wt901.yml 파일을 바꿔줍니다.  

```bash
cd ~/fast-lio-STUDY/240816/witmotion_imu/
cp wt901_launch.py ~/ros2_ws/src/witmotion_ros/launch/
cp wt901.yml ~/ros2_ws/src/witmotion_ros/config/
cd ~/ros2_ws
cbp witmotion_ros
humble
```
<br/>
<br/>
<br/>

 > rule 적용  

```bash
cd ~/fast-lio-STUDY/240816/witmotion_imu/scripts/
./create_udev_rules.sh
```
<br/>
<br/>
<br/>

 > 실행  

```bash
ros2 launch witmotion_ros wt901_launch.py 
```

<br/>
<br/>
<br/>

 > 토픽 데이터 확인

```bash
ros2 topic echo /imu
```

