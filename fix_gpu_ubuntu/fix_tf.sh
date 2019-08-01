#!/bin/bash


if [ ! -f "/usr/lib/x86_64-linux-gnu/libcublas.so.10.0" ]
then
	ln -s /usr/lib/x86_64-linux-gnu/libcublas.so.10 /usr/lib/x86_64-linux-gnu/libcublas.so.10.0
else
	echo "/usr/lib/x86_64-linux-gnu/libcublas.so.10.0 exists"
fi

if [ ! -f "/usr/lib/x86_64-linux-gnu/libcusolver.so.10.0" ]
then
	ln -s /usr/local/cuda-10.1/targets/x86_64-linux/lib/libcusolver.so.10 /usr/local/cuda-10.1/targets/x86_64-linux/lib/libcusolver.so.10.0
else 
	echo "/usr/local/cuda-10.1/targets/x86_64-linux/lib/libcusolver.so.10.0 exists"
fi

if [ ! -f "/usr/local/cuda-10.1/targets/x86_64-linux/lib/libcudart.so.10.0" ]
then
	sudo ln -s /usr/local/cuda-10.1/targets/x86_64-linux/lib/libcudart.so.10.1 /usr/local/cuda-10.1/targets/x86_64-linux/lib/libcudart.so.10.0
else
	echo "/usr/local/cuda-10.1/targets/x86_64-linux/lib/libcudart.so.10.0 exists"
fi




