# K-Means-Steganography: Secure Data Transmission using Steganography and Cryptography

## Introduction
The objective of this project is to take data, encrypt it, and hide it over an image before sending it to the receiver.
This is done using a combination of optimized techniques of Cryptography and Steganography. 

1. Cryptography reorders/replaces the data such that it becomes difficult to recover the original data without a key. 
2. Steganography hides the data within other media making it less obvious that any sort of secret data exists. This made up the motivation to benefit from both, i.e. combining cryptography and steganography for data transmission.

## Algorithms Used
### AES Algorithm
Standard AES-128-bit algorithm is used to encrypt the data.

### K-Means Algorithm
For the Steganography part, we use the K-Means clustering algorithm to divide the cover image into clusters. Then the message to be transmitted is divided into parts equal to the number of clusters. The data for a cluster is then hidden in the Least Significant Bit(LSB) of the pixels belonging to that cluster.

## Architecture 
![Architecture](https://github.com/deveshv-99/K-Means-Steganography/assets/135348080/9720326a-db9f-4b0e-892b-ade2be8f700f)

## Execution
The Major_Project.ipynb file contains the entire codebase. It has functions for both the sender and receiver side. This was run on a Google Colab notebook instance.
