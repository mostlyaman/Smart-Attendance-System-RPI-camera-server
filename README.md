# Smart-Attendance-System-RPI-camera-server

Code for Smart Attendance System Camera Server.

Change the code within the /capture api to serve your own image using a camera. Only encode the image to base64 as demonstrated.
Run the server using the following command to connect multiple raspberry pi camera servers to the master bluetooth node (mostlyaman/Smart-Attendance-System-RPI-master).

```sh
flask run --host=0.0.0.0
```
