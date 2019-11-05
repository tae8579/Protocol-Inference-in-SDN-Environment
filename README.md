# Protocol-Inference-in-SDN-Environment
This project proposes an architecture of protocol Inference in SDN environment.

## Introduction
This is Network Protocol Inference of aSTEAM Project (Next-Generation Information Computing Development Program through the National Research Foundation of Korea (NRF) funded by the Ministry of Science and ICT). 

This software constructs SDN environment and inferences protocol state from unknown protocols.

## Requirements and Dependencies
* OS : `Ubuntu 16.04.6 LTS` ~ `Ubuntu 18.04.1 LTS`
* Language : `Python`
* Library : `KU-S-S-EM`, `KU-S-S-IM`, `Floodlight`, `Mininet`

## Instructions
* Instructions for Use of `Protocol-Inference-in-SDN-Environment`

> Install Mininet & Floodlight
  1. Install Mininet refer to `https://github.com/mininet/mininet`
  2. Install Floodlight refer to `https://github.com/floodlight/floodlight`
  
> Constructs SDN Environment through `Topology/topology.py`
  1. Run `Python topology.py`
  
> Routing Using SDN Controller through `SDN Controller/Control/flow_contol`  
  1. Run `Python flow_contol.py` in Mininet
  
> Start Video Streaming Service through `Service/Video Streaming/client.py, server.py`  
  1. Run `Python server.py` in Mininet
  2. Run `Python client.py` in Mininet
  
> We are working on Protocol Inference.. :(
  
