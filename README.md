The project developed for indoor localization using the Visible light communication using embedded and machine learning approach, 
Position systems is very important in today’s world. Position systems providing many services not only for localizing the object, but for many Location based services (LBS) including public safety, consumer services and in enterprises services. Position system using GPS also play an important role in next generation self driving car. GPS is widely used system worldwide for position applications. But, GPS accuracy is not same  inside as it gives in outdoor environment i.e. hospitals, big infrastructure, big shopping mall etc. that’s why the concept for indoor localization have became an important area for positioning. That can be used for visually impaired people to locate, in indoor navigation and in disaster management etc. So there are many research have been proposed with different technologies in order to achieve high accuracy in indoor localization.
In next generation for internet of things (IoT) where demand for high bandwidth and fast speed for data communication will increases. So the existing technology where we are mostly depend on radio frequency will not be sufficient for such requirement as the number of user’s and devices will be increased. So we need some other solutions that can be used to fulfill the aforesaid requirements. Visible light communication (VLC) that became an emerging research area for data communication can be used for high speed and bandwidth as compared to radio waves. 
The proposed technology for data communication will be used in near future that we call as (Light fidelity) Li-Fi. So in increasing demand for indoor localization motivates to use this technology. In this project VLC based method is used for indoor localization where we have tried to obtain the results using embedded approach. So we will be able to localize the object in indoor environment.                      
 
VLC is data communication that uses the visible spectrum between 400 to 780 nm (400-800 THz) as shown in Figure 2.1. Speed of the VLC is almost same as the speed of the light, so, data can communicate very fast. As, another advantage of VLC is high spectrum as compare to radio waves i.e., 10,000 times larger [4]. VLC has no electromagnetic interference so it can be used in Hospitals, Power plants and so on. There are also some disadvantages of VLC like it is difficult to use for large distances, Interference from higher light source bulbs, sun light and Line of sight.   
 ![image](https://user-images.githubusercontent.com/32608510/38634698-f3b3736e-3de0-11e8-82a7-7129f587fb59.png)
 
 ## Prerequisite
 1. Raspberry Pi: Controller for processing
 
 2. ADS1115 Adafruit ADC controller: To read analog input in raspberry Pi
 3. OPT101 Photodiode: Measures the light intensity, used as receiver 
 4. LEDs: High on/off capability used as transmitter

## Technical literature 
 1.	Fast fourier transform (FFT)- FFT algorithm converts the time domain signal to frequency domain, It computes the discrete fourier   transform (DFT) sequence. FFT is the less complex in computation as compared to DFT.  
 2.	Frequency division multiplexing (FDM) in LED: LED are can be used transmitter, So in order to differentiate different transmitter different multiplexing can be used i.e. Time division multiplexing (TDM), Code division multiplexing (CDMA), Color division multiplexing, Frequency division multiplexing (FDM), Space division multiplexing. 
 3.Received Signal Strength (RSS): 
 4.	Trilateration: Triangulation uses geometric properties of the triangles in order to estimate the position. There are two derivation of the triangulation: lateration and angulation. Lateration method involves time of arrival (TOA), time difference of arrival (TDOA) and received signal strength (RSS) to estimate the position of target device. Angulation measures angles relative to several reference points angle of arrival (AOA) in order to estimate the position of target device.      
![image](https://user-images.githubusercontent.com/32608510/38749818-95c6e952-3f70-11e8-94ac-668cf6849016.png) Fig. 2 Trilateration model
