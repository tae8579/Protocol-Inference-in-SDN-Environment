# Protocol-Inference-in-SDN-Environment
This project proposes an architecture of protocol Inference in SDN environment.

## Introduction
This is Network Protocol Inference of aSTEAM Project (Next-Generation Information Computing Development Program through the National Research Foundation of Korea (NRF) funded by the Ministry of Science and ICT). 

This software constructs SDN environment and inferences protocol state from unknown protocols.
It basically consists of two sub-module referencing our KU-S-S-EM, KU-S-S-IM projects. This project is a whole framework to test and verify protocol inference function with SDN environment using Floodlight and Mininet. Detailed instructions for running every softwares in this project are given below, and detailed implementaions and alogrithms of each sub module are demonstrated in KU-S-S-EM and KU-S-S-IM submodule project. The overall architecture is shown below.

![image](https://user-images.githubusercontent.com/6499345/68915370-1dd94d00-07a5-11ea-9b06-b6018e1f768e.png)



## Requirements and Dependencies
* OS : `Ubuntu 16.04.6 LTS` ~ `Ubuntu 18.04.1 LTS`
* Language : `Python`
* Library : `KU-S-S-EM`, `KU-S-S-IM`, `Floodlight`, `Mininet`

## Instructions
* Instructions for Use of `Protocol-Inference-in-SDN-Environment`

> Install Mininet & Floodlight
  1. Install Mininet refer to `https://github.com/mininet/mininet`
  2. Install Floodlight refer to `https://github.com/floodlight/floodlight`
  3. Run `mininet` and `floodlight`
  
> Constructs SDN Environment through `Topology/topology.py`
  1. Run `Python topology.py`
  
> Routing Using SDN Controller through `SDN Controller/Control/flow_contol`  
  1. Run `Python flow_contol.py` in mininet
  
> Start Video Streaming Service through `Service/Video Streaming/client.py, server.py`  
  1. Run `Python server.py` in mininet
  2. Run `Python client.py` in mininet
  
> We are working on Protocol Inference.. :)
