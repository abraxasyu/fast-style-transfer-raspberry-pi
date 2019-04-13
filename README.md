See: https://github.com/lengstrom/fast-style-transfer for all details on the style transfer

Obviously, you will need a webcam for this. The image display is done via pygame.

Go into the cloned local directory and type: "python process.py"

On my (raspberry pi 3)[https://www.amazon.com/gp/product/B00MQLB1N6/ref=oh_aui_search_asin_title?ie=UTF8&psc=1] B+, each frame takes ~30 seconds to process.

Next steps would be to make the model much faster, e.g. using mobilenet or by using other techniques.
