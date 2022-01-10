# vag-canbus
Reads the VAG infotainment canbus and triggers key strokes to control Open Auto Pro, codes are for Skoda Yeti 5L 2011

## Infotainment bus
* 291 # 0A AA 02 00 00 / 0A 55 04 00 00 doorlock READONLY
* 635 light
* 35b byte 5 (20 28) clutch
* 351 byte 1 (00 02) reverse
* 5C1 steering wheel controls
* 571 panoramic roof (read only) 
* 575 byte 4 clutch
* 369 revs

## Convenience bus
* 381#A0.0F.00.84.00.00 open door
* 381#A0.0F.00.84.00.00 close door
* 181#xx.00 -> (04,01,08,02) front left window (short down, short up, long down, long up)
* 181#xx.00 -> (40,10,80,20) front right window
* 181#00.xx -> (40,10,80,20) rear right window
* 181#xx.00 -> (04,01,08,02) rear left window
* 2C3#xx -> 01 IGN OFF | 07 IGN ON
* 5DD xx.00.90.00.00 -> 2D lights on (read only)
* 635#xx.xx.AF -> 2D lights on
