PULSONIX_LIBRARY_ASCII "SamacSys ECAD Model"
//440631/310146/2.50/2/4/Diode

(asciiHeader
	(fileUnits MM)
)
(library Library_1
	(padStyleDef "r235_155"
		(holeDiam 0)
		(padShape (layerNumRef 1) (padShapeType Rect)  (shapeWidth 1.55) (shapeHeight 2.35))
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
	(patternDef "DIOM5226X230N" (originalName "DIOM5226X230N")
		(multiLayer
			(pad (padNum 1) (padStyleRef r235_155) (pt -2.15, 0) (rotation 90))
			(pad (padNum 2) (padStyleRef r235_155) (pt 2.15, 0) (rotation 90))
		)
		(layerContents (layerNumRef 18)
			(attr "RefDes" "RefDes" (pt 0, 0) (textStyleRef "Normal") (isVisible True))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt -3.575 1.71) (pt 3.575 1.71) (width 0.05))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt 3.575 1.71) (pt 3.575 -1.71) (width 0.05))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt 3.575 -1.71) (pt -3.575 -1.71) (width 0.05))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt -3.575 -1.71) (pt -3.575 1.71) (width 0.05))
		)
		(layerContents (layerNumRef 28)
			(line (pt -2.598 1.302) (pt 2.598 1.302) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt 2.598 1.302) (pt 2.598 -1.302) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt 2.598 -1.302) (pt -2.598 -1.302) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt -2.598 -1.302) (pt -2.598 1.302) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt -2.598 0.528) (pt -1.822 1.302) (width 0.025))
		)
		(layerContents (layerNumRef 18)
			(line (pt 2.598 1.302) (pt -2.925 1.302) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt -2.598 -1.302) (pt 2.598 -1.302) (width 0.2))
		)
	)
	(symbolDef "B250A-13-F" (originalName "B250A-13-F")

		(pin (pinNum 1) (pt 0 mils 0 mils) (rotation 0) (pinLength 100 mils) (pinDisplay (dispPinName false)) (pinName (text (pt 140 mils -15 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 2) (pt 600 mils 0 mils) (rotation 180) (pinLength 100 mils) (pinDisplay (dispPinName false)) (pinName (text (pt 460 mils -15 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(line (pt 200 mils 100 mils) (pt 200 mils -100 mils) (width 6 mils))
		(line (pt 100 mils 0 mils) (pt 200 mils 0 mils) (width 6 mils))
		(line (pt 400 mils 0 mils) (pt 500 mils 0 mils) (width 6 mils))
		(poly (pt 200 mils 0 mils) (pt 400 mils 100 mils) (pt 400 mils -100 mils) (pt 200 mils 0 mils) (width 10  mils))
		(attr "RefDes" "RefDes" (pt 450 mils 200 mils) (justify Left) (isVisible True) (textStyleRef "Normal"))
		(attr "Type" "Type" (pt 450 mils 100 mils) (justify Left) (isVisible True) (textStyleRef "Normal"))

	)
	(compDef "B250A-13-F" (originalName "B250A-13-F") (compHeader (numPins 2) (numParts 1) (refDesPrefix D)
		)
		(compPin "1" (pinName "K") (partNum 1) (symPinNum 1) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "2" (pinName "A") (partNum 1) (symPinNum 2) (gateEq 0) (pinEq 0) (pinType Unknown))
		(attachedSymbol (partNum 1) (altType Normal) (symbolName "B250A-13-F"))
		(attachedPattern (patternNum 1) (patternName "DIOM5226X230N")
			(numPads 2)
			(padPinMap
				(padNum 1) (compPinRef "1")
				(padNum 2) (compPinRef "2")
			)
		)
		(attr "Manufacturer_Name" "Diodes Inc.")
		(attr "Manufacturer_Part_Number" "B250A-13-F")
		(attr "Mouser Part Number" "621-B250A-F")
		(attr "Mouser Price/Stock" "https://www.mouser.co.uk/ProductDetail/Diodes-Incorporated/B250A-13-F?qs=vCs%252BXXHcZCYwSuq4TGO9ug%3D%3D")
		(attr "Arrow Part Number" "B250A-13-F")
		(attr "Arrow Price/Stock" "https://www.arrow.com/en/products/b250a-13-f/diodes-incorporated?region=nac")
		(attr "Description" "Diodes Inc B250A-13-F, SMT Schottky Diode, 50V 2A, 2-Pin DO-214AC")
		(attr "<Hyperlink>" "https://www.diodes.com/assets/Datasheets/ds13004.pdf")
		(attr "<Component Height>" "2.3")
		(attr "<STEP Filename>" "B250A-13-F.stp")
		(attr "<STEP Offsets>" "X=0;Y=0;Z=0")
		(attr "<STEP Rotation>" "X=0;Y=0;Z=0")
	)

)
