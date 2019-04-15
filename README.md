Not-so-realtime style transfer on Raspberry Pi

Using...
* fswebcam for image capture (You'll need a webcam)
* pygame for display handling
* (lengstrom's fast-style transfer)[https://github.com/lengstrom/fast-style-transfer] for style transfer

To use...
* clone repo
* cd into cloned local directory and type: "python process.py"

On my (raspberry pi 3)[https://www.amazon.com/gp/product/B00MQLB1N6/ref=oh_aui_search_asin_title?ie=UTF8&psc=1] B+, each frame takes ~30 seconds to process.

Next steps would be to make the model much faster, e.g. using mobilenet or by using other techniques.
