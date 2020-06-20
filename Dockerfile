FROM centos
RUN yum install python36 -y
RUN pip3 install --upgrade pip
RUN pip3 install tensorflow
RUN pip3 install keras
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install pillow
RUN pip3 install matplotlib
ENTRYPOINT ["python3"]
CMD ["/models/mlops_model.py"]
