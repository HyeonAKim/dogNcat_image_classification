# 이미지 판별 튜토리얼

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [이미지 판별 튜토리얼](#이미지-판별-튜토리얼)
  * [1. 도커에서 텐서플로우 및 필요 패키지 다운로드](#1-도커에서-텐서플로우-및-필요-패키지-다운로드)
    * [1. 텐서플로우 설치](#1-텐서플로우-설치)
    * [2. 이미지 분류 폴더 압축풀기](#2-이미지-분류-폴더-압축풀기)
    * [3.imageMagicK 설치](#3imagemagick-설치)
  * [2. 구글에서 이미지 크롤링](#2-구글에서-이미지-크롤링)
    * [1.크롤링을 위한 패키지를 설치하자.](#1크롤링을-위한-패키지를-설치하자)
    * [2. 이미지크롤러 실행](#2-이미지크롤러-실행)
  * [3. 수집된 이미지 파일 형식 변환](#3-수집된-이미지-파일-형식-변환)
  * [4. jpg 파일 TFRecord 파일로 변환](#4-jpg-파일-tfrecord-파일로-변환)
  * [5. inception 모델 사용](#5-inception-모델-사용)
  * [6. 개고양이 이미지 학습](#6-개고양이-이미지-학습)
  * [7. 새로운 이미지 예측](#7-새로운-이미지-예측)

<!-- tocstop -->

## 1. 도커에서 텐서플로우 및 필요 패키지 다운로드

### 1. 텐서플로우 설치
텐서플로우가 설치된 리눅스 이미지를 다운 받고 경로 및 포트를 설정한다.

- 윈도우 공유폴더 : /c/Users/User/docker/slim
- 리눅스 공유폴더 : /root/
- 쥬피터노트북 포트 : (기본 8888)
- 텐서보드 포트 : (기본 6006)

```
docker run -it -v /c/Users/User/docker/slim:/root/ -p 8888:8888 -p 6006:6006 --name=dl1 tensorflow/tensorflow:latest-devel
```

### 2. 이미지 분류 폴더 압축풀기

소스파일을 가져오자.
```
cd ~ 
git clone https://github.com/HyeonAKim/dogNcat_image_classification
```


### 3.imageMagicK 설치

imagemagick를 설치하자

```
apt-get install imagemagick
```
![이미지 116](http://i.imgur.com/UOavklh.png)

> vi 명령어가 실행이 안될 수도 있으니 다음과 같이 실행한다.
apt-get install vim


## 2. 구글에서 이미지 크롤링

### 1.크롤링을 위한 패키지를 설치하자.

```
pip install icrawler
```
![이미지 112](http://i.imgur.com/5AE2i21.png)

### 2. 이미지크롤러 실행

```
python models/slim/image_crawler.py
```
![이미지 113](http://i.imgur.com/O49mKl4.png)
...
![이미지 114](http://i.imgur.com/cC54FEI.png)

이미지가 잘 수집되어있는지 경로에 가서 확인해보자
>윈도우 : /c/Users/User/docker/slim/data
리눅스 : /root/data/

## 3. 수집된 이미지 파일 형식 변환
수집된 이미지 파일을 보면 png, gif, jpeg, ashx 등의 파일이 다양하게 있다.
이 파일들을 imagemagick 를 이용하여 jpg 로 변환한다.
일괄적으로 변환하는 dojpg.sh 파일을 실행한다.

.sh 경로
>윈도우 :  /c/Users/User/docker/slim/
리눅스: /root/do.jpg

```
. dojpg.sh
```
이미지 파일들이 모두 jpg 형식으로 바껴져 있는것을 확인할 수 있다.

![이미지 117](http://i.imgur.com/mkU0L0l.png)

이미지들을 보게 되면 깨져 있는 파일들이 있을 수 있다. 확인하고 반드시 삭제해주자.


## 4. jpg 파일 TFRecord 파일로 변환
TFRecord 변환하고 폴더명을 라벨로 하여 데이터를 변환한다.

변환된 TFRecord가 저장될 경로를 DATA_DIR로 설정한다.

```
cd ~
DATA_DIR=/root/data/dogNcat
```

파일변환 .py코드를 실행한다.
```
python models/slim/convert_data.py \
--dataset_name=dogNcat \
--dataset_dir="${DATA_DIR}"
```

![이미지 118](http://i.imgur.com/IQPkqCm.png)

분석에 사용할 데이터변환 작업은 끝났다.

## 5. inception 모델 사용
inception은 구글에서 생성한 이미지 분류 모델이다. 이 모델을 가지고와서 개고양이 이미지를 학습하여 예측에 활용할 것이다.

모델을 다운받은 download_inception.py를 실행하자.
```
python /root/models/slim/download_inception.py
```
![이미지 119](http://i.imgur.com/gc7CA6A.png)

## 6. 개고양이 이미지 학습

학습 파일을 실행시킨다.

```
python /root/models/slim/learn_dogNcat.py
```
![이미지 121](http://i.imgur.com/efGWuPi.png)

새롭게 학습된 모델을 보자 .
> 경로
윈도우 : C:\Users\User\docker\slim\inception_model\inception_dogNcat
리눅스 :  /root/inception_model/inception_dogNcat/

![이미지 122](http://i.imgur.com/4clY3HD.png)

## 7. 새로운 이미지 예측

학습된 모델을 사용해서 이미지를 예측해보자.
예측에 사용되는 코드를 실행하고 flag 값으로 이미지 주소를 입력한다.

```
python /root/models/slim/predict_dogNcat.py \ --image_url='http://newsimg.wowtv.co.kr/20170203/B20170203131507900.jpg'
```
![enter image description here](http://newsimg.wowtv.co.kr/20170203/B20170203131507900.jpg)

![이미지 124](http://i.imgur.com/28ickmk.png)

## 8.텐서보드 실행
