PULSONIX_LIBRARY_ASCII "SamacSys ECAD Model"
//688316/310146/2.50/3/3/LED

(asciiHeader
	(fileUnits MM)
)
(library Library_1
	(padStyleDef "r330_50"
		(holeDiam 0)
		(padShape (layerNumRef 1) (padShapeType Rect)  (shapeWidth 0.500) (shapeHeight 3.300))
		(padShape (layerNumRef 16) (padShapeType Ellipse)  (shapeWidth 0) (shapeHeight 0))
	)
	(padStyleDef "r330_130"
		(holeDiam 0)
		(padShape (layerNumRef 1) (padShapeType Rect)  (shapeWidth 1.300) (shapeHeight 3.300))
		(padShape (layerNumRef 16) (padShapeType Ellipse)  (shapeWidth 0) (shapeHeight 0))
	)
	(textStyleDef "Normal"
		(font
			(fontType Stroke)
			(fontFace "Helvetica")
			(fontHeight 1.27)
			(strokeWidth 0.127)
		)
	)
	(patternDef "LTPLC034UVH405" (originalName "LTPLC034UVH405")
		(multiLayer
			(pad (padNum 1) (padStyleRef r330_50) (pt 1.400, 0.000) (rotation 0))
			(pad (padNum 2) (padStyleRef r330_50) (pt -1.400, 0.000) (rotation 0))
			(pad (padNum 3) (padStyleRef r330_130) (pt 0.000, 0.000) (rotation 0))
		)
		(layerContents (layerNumRef 18)
			(attr "RefDes" "RefDes" (pt 0.000, 0.000) (textStyleRef "Normal") (isVisible True))
		)
		(layerContents (layerNumRef 28)
			(line (pt 1.725 1.725) (pt -1.725 1.725) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt -1.725 1.725) (pt -1.725 -1.725) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt -1.725 -1.725) (pt 1.725 -1.725) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt 1.725 -1.725) (pt 1.725 1.725) (width 0.025))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt 2.725 2.725) (pt -2.725 2.725) (width 0.1))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt -2.725 2.725) (pt -2.725 -2.725) (width 0.1))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt -2.725 -2.725) (pt 2.725 -2.725) (width 0.1))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt 2.725 -2.725) (pt 2.725 2.725) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(line (pt 2.3 0) (pt 2.3 0) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(arc (pt 2.25, 0) (radius 0.05) (startAngle -.0) (sweepAngle 180.0) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(line (pt 2.2 0) (pt 2.2 0) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(arc (pt 2.25, 0) (radius 0.05) (startAngle 180.0) (sweepAngle 180.0) (width 0.1))
		)
	)
	(symbolDef "LTPL-C034UVH405" (originalName "LTPL-C034UVH405")

		(pin (pinNum 1) (pt 0 mils -200 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -225 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 2) (pt 0 mils 0 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -25 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 3) (pt 0 mils -100 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -125 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(line (pt 200 mils 100 mils) (pt 600 mils 100 mils) (width 6 mils))
		(line (pt 600 mils 100 mils) (pt 600 mils -300 mils) (width 6 mils))
		(line (pt 600 mils -300 mils) (pt 200 mils -300 mils) (width 6 mils))
		(line (pt 200 mils -300 mils) (pt 200 mils 100 mils) (width 6 mils))
		(attr "RefDes" "RefDes" (pt 650 mils 300 mils) (justify Left) (isVisible True) (textStyleRef "Normal"))
		(attr "Type" "Type" (pt 650 mils 200 mils) (justify Left) (isVisible True) (textStyleRef "Normal"))

	)
	(compDef "LTPL-C034UVH405" (originalName "LTPL-C034UVH405") (compHeader (numPins 3) (numParts 1) (refDesPrefix LED)
		)
		(compPin "1" (pinName "K") (partNum 1) (symPinNum 1) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "2" (pinName "A") (partNum 1) (symPinNum 2) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "3" (pinName "EP") (partNum 1) (symPinNum 3) (gateEq 0) (pinEq 0) (pinType Unknown))
		(attachedSymbol (partNum 1) (altType Normal) (symbolName "LTPL-C034UVH405"))
		(attachedPattern (patternNum 1) (patternName "LTPLC034UVH405")
			(numPads 3)
			(padPinMap
				(padNum 1) (compPinRef "1")
				(padNum 2) (compPinRef "2")
				(padNum 3) (compPinRef "3")
			)
		)
		(attr "Manufacturer_Name" "Lite-On")
		(attr "Manufacturer_Part_Number" "LTPL-C034UVH405")
		(attr "Mouser Part Number" "859-LTPL-C034UVH405")
		(attr "Mouser Price/Stock" "https://www.mouser.co.uk/ProductDetail/Lite-On/LTPL-C034UVH405?qs=rrS6PyfT74dhK6mT7j3K8A%3D%3D")
		(attr "Arrow Part Number" "LTPL-C034UVH405")
		(attr "Arrow Price/Stock" "https://www.arrow.com/en/products/ltpl-c034uvh405/lite-on-technology?region=nac")
		(attr "Description" "Ultraviolet (UV) Emitter 405nm 3.7V 700mA 130 2-SMD, No Lead Exposed Pad")
		(attr "<Hyperlink>" "https://optoelectronics.liteon.com/upload/download/DS23-2015-0073/LTPL-C034UVH405%20DataSheet.PDF")
		(attr "<Component Height>" "2.33")
		(attr "<STEP Filename>" "LTPL-C034UVH405.stp")
		(attr "<STEP Offsets>" "X=0;Y=0;Z=0")
		(attr "<STEP Rotation>" "X=0;Y=0;Z=0")
	)

)