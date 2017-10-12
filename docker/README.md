# How to use the Docker image

## Building

```
$   cd  bigdl-tutorials/docker
$   docker build .
$   docker images
```

## Running it

```
$   docker images
```
Will list all images.  

#### Option 1:
The simplest way to run the docker container is to use `run-bigdl-docker.sh` script at the project root directory.  It will run the image and also mounts a working directory so all the work is saved automatically.

```
    $    ./run-bigdl-docker.sh   <image_id>
```

#### Option 2:
Running the Jupyter notebook by default  (~/run_jupyter.sh)
```
    $   docker run -it  -p 8888:8888   IMAGE_ID
```

#### Option 3:
Shell access
```
    $   docker run -it  -p 8888:8888   IMAGE_ID   bash
```

In Docker container you can run Jupyter as follows
```
    $    ./run_jupyter.sh
```

Go to http://localhost:8888  in browser
