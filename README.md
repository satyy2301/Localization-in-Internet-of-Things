INTRODUCTION
The position estimation is an essential component of wireless sensor networks applications,
especially in the environmental monitoring applications such as: animal dwelling place
monitoring, water quality monitoring and farming precision. In addition, the location information
enables various emerging applications such as inventory management, intrusion detection, road
traffic tracking, health monitoring, etc. Methods used to determine the position are usually based
on geometric calculations such as triangulation (by measuring angles with respect to fixed points
or nodes with known position) and trilateration (by measuring the distance between nodes). In
order to determine the distance between two nodes, several techniques can be employed, such as
synchronization, radio signal strength and the physical characteristics of the carrying wave. The
localization techniques in the WSNs can be free of a previous position determination in the
network, relying on a few specific sensors’ position information and their inter-measurements in
the network such as time difference of arrival, distance, angle of arrival, and connectivity. The
prior known localization information sensors are called anchors or references where their
locations can be obtained through a global positioning system (GPS), or installing anchors at
points with known coordinates. Localization in wireless sensor networks applications is a
well-addressed research problem in the literature. Indeed, equipping all the sensors with
positioning systems or GPS is expensive in terms of energy due to a high-energy consumption by
the GPS. In addition, the GPS services are not available in some area such as the indoor
environment. A more efficient alternative is to provide only a smaller number of position-known
sensors (equipped with GPS, or fixed known-position devices) and locating the other sensors by
interchanging information with the anchors. Several methods based on anchors are suggested in
the literature like Bayesian approaches of Monte Carlo. They consist of generating particles to
cover the solution area. However, the main drawback of such methods is their bulk
over-consumption in order to save all the particles. While the device-based techniques have
advanced remarkably toward better localization performance, the device-free techniques are
more favorable in various important applications. For instance, if an anomaly object exists in an
area of interest, the intrusion detection and tracking are equally identified. Another example of
device-free localization is the safety precaution of solitary seniors or disabled people in
emergencies such as empyrosis, fall, apoplexy, etc. Thus, there is an emerging need for a
profitable as well as adequate device-free positioning tool. The distinct features of device free
techniques bring new challenges in localization. In this paper, we discuss key issues and inherent
challenges facing localization approaches, techniques and technology of localization in the
WSN. We study the existing localization systems, both device-free and device-based, which use
different technologies such as UWB radar and ultrasound, and which are based on different
techniques such as centralized, distributed and iterative localization techniques.
PROBLEM STATEMENT
The proliferation of Internet of Things (IoT) devices has led to an increased demand for precise
location estimation, particularly in applications such as environmental monitoring, inventory
management, intrusion detection, and health monitoring. Traditional methods, such as Global
Positioning System (GPS), can be costly, energy-intensive, and may not be applicable in indoor
environments. While device-based techniques have advanced, there is a need for efficient and
cost-effective device-free positioning tools, especially in scenarios involving the safety of
individuals during emergencies or the monitoring of anomaly objects. The challenges faced by
existing IoT localization approaches include issues of energy consumption, accuracy, and
adaptability to diverse environments.
MOTIVATION
The motivation behind addressing these challenges lies in the wide-ranging applications of IoT
and the imperative for accurate location information. Various sectors, including environmental
monitoring, agriculture, and healthcare, benefit from precise location data for effective
decision-making and automation. The limitations of traditional GPS-based methods in IoT
deployments, coupled with the energy demands of equipping all devices with GPS, highlight the
urgency of exploring alternative localization techniques. Additionally, the need for device-free
localization techniques is underscored by scenarios where tracking the presence and movement
of objects or individuals without specific devices is crucial. Solving these challenges will not
only enhance the efficiency of IoT applications but also unlock new possibilities for innovative
solutions in areas such as smart cities, healthcare, and emergency response systems.
REQUIREMENTS
Hardware Requirements:
● Raspberry pi
● Arduino
Software Requirements:
● Python Libraries
