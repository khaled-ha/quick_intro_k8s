# basic commands
Basic commands :
    kubectl get pods
    kubectl get pods -o wide

    kubectl get svc
    kubectl create deployment k8s-web-hello --image=khaledhadjali/k8s-web-hello
    kubectl expose deployment k8s-web-hello --type=NodePort  --port=3000

    kubectl delete service k8s-web-hello
    
    kubectl expose deployment k8s-web-hello --type=LoadBalancer  --port=3000 
    
    kubectl set image deployment k8s-web-hello k8s-web-hello=khaledhadjali/k8s-web-hello
    
    kubectl set image deployment k8s-web-hello k8s-web-hello=khaledhadjali/k8s-web-hello:2.0.0
    kubectl rollout status deployment k8s-web-hello

    minikube service k8s-web-hello

How to get minikube ip:
    minikube ip

How to access minikube pod:
    ssh -v docker@192.168.59.100


How to build your image:
    docker build  . -t khaledhadjali/k8s-web-hello
    docker push khaledhadjali/k8s-web-hello 
    docker build  . -t khaledhadjali/k8s-web-hello:2.0.0
    docker push khaledhadjali/k8s-web-hello:2.0.0

# to start minikube with a specefic driver
minikube start --driver=virtualbox
minikube stop

alias k=kubectl
k describe node
k delete -f k8s-web-to-nginx.yml -f nginx.yml
k apply -f k8s-web-to-nginx.yml -f nginx.yml
minikube service k8s-web-to-nginx

docker build  . -t khaledhadjali/k8s-web-to-nginx
docker push khaledhadjali/k8s-web-to-nginx

# how to exec command inside pod container
k exec k8s-web-to-nginx-77689c6774-pxtdv --nslookup nginx
k exec k8s-web-to-nginx-77689c6774-pxtdv -- nslookup nginx



python fast api : 

    docker build  . -t khaledhadjali/k8s-hello-fastapi
    docker run -p 8000:8000 -i -t khaledhadjali/k8s-hello-fastapi:latest 

