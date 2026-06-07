---
title: Hardware
permalink: /Hardware/
author_profile: false
layout: splash
---
{% include figure popup=true image_path="/images/npa1_hardware_lr.jpg" alt="NPA1 Hardware" caption="Example of a station setup using a Raspberry Pi 3+, Mosaic X5, and a temperature and pressure logger." %}

Our system is built around high-quality sensors, with data logging and real-time access managed by a Raspberry Pi 3+. We deliberately use the older Raspberry Pi 3+ model due to its lower power consumption, which we also monitor as part of the setup. Real-time data is available for most sites via local Wi-Fi or a SIM connection.

The GNSS component is the Septentrio Mosaic X5, a compact multi-constellation receiver module, typically paired with a Harxon GPS 1000 survey antenna. Meteorological data are collected using a Bosch BMP388 (barometric pressure and altitude) and an ASAIR temperature sensor, with data processing handled by an Adafruit Feather. We also have used (and still use) an ublox ZED-F9P sensor at some sites.

All software was developed at the University of Potsdam.

{% include figure popup=true image_path="/images/hydro_sensor_lr.jpg" alt="" caption="Hydrology Sensor." %}

{% include figure popup=true image_path="/images/npa7_hardware_lr.jpg" alt="" caption="We house the hardware in multiple enclosures to ensure safe operation, and include a 12V backup battery to maintain functionality during power outages." %}

