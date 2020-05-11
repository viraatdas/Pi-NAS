# Pi-NAS

The project is intended to fashion a Raspberry Pi into a NAS. 

### General Interface
This will be analogous to Airdrop. 

Essentially multiple people can connect to the Pi network with the intention to either **receive** or **send** files.

To connect to the network, the person must specify if they want to either receive or send the file. 

#### Connecting for the first time
First time configuration will simply require the user to specify a unique name. This will be the identifier that will 
be shown to everyone else on the network. Additionally, they'll set a *download* directory. 

#### Send
A user will be displayed the users currently connected to the network or have the option to type the unique name in 
of the person they want to send the file to. 

#### Receive
Once the sender sends the file, they will be prompted if they want to receive the file or not. 

##### Note
Chance is that this project might not be used on a Pi and potentially on an old laptop