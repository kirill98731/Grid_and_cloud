#!/bin/bash
az vm start --resource-group MyResourceGroup_1 --name MyVm_1
ssh azureuser@13.92.158.174 python main.py
az vm stop --resource-group MyResourceGroup_1 --name MyVm_1