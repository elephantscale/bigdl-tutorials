# How to use the Docker image

## Building

```
$   cd  bigdl-labs/docker
$   docker build .
$   docker images
```

## Running it

```
$   docker images
```
Will list all images.  

Running the Jupyter notebook by default  (~/run_jupyter.sh)
```
    $   docker run -it  -p 8888:8888   IMAGE_ID
```

Shell access
```
    $   docker run -it  -p 8888:8888   IMAGE_ID   bash
```

In Docker container
```
    $    ./run_jupyter.sh
```

Go to http://localhost:8888  in browser
