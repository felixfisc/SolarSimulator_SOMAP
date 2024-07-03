PULSONIX_LIBRARY_ASCII "SamacSys ECAD Model"
//7177770/310146/2.50/3/3/LED

(asciiHeader
	(fileUnits MM)
)
(library Library_1
	(padStyleDef "r270_50"
		(holeDiam 0)
		(padShape (layerNumRef 1) (padShapeType Rect)  (shapeWidth 0.500) (shapeHeight 2.700))
		(padShape (layerNumRef 16) (padShapeType Ellipse)  (shapeWidth 0) (shapeHeight 0))
	)
	(padStyleDef "r270_100"
		(holeDiam 0)
		(padShape (layerNumRef 1) (padShapeType Rect)  (shapeWidth 1.000) (shapeHeight 2.700))
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
	(patternDef "SST10FRB130J730" (originalName "SST10FRB130J730")
		(multiLayer
			(pad (padNum 1) (padStyleRef r270_50) (pt 0.000, 1.100) (rotation 90))
			(pad (padNum 2) (padStyleRef r270_50) (pt 0.000, -1.100) (rotation 90))
			(pad (padNum 3) (padStyleRef r270_100) (pt 0.000, 0.000) (rotation 90))
		)
		(layerContents (layerNumRef 18)
			(attr "RefDes" "RefDes" (pt 0.000, 0.000) (textStyleRef "Normal") (isVisible True))
		)
		(layerContents (layerNumRef 28)
			(line (pt -1.725 -1.725) (pt 1.725 -1.725) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt 1.725 -1.725) (pt 1.725 1.725) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt 1.725 1.725) (pt -1.725 1.725) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt -1.725 1.725) (pt -1.725 -1.725) (width 0.025))
		)
		(layerContents (layerNumRef 18)
			(line (pt -1.725 1.725) (pt 1.725 1.725) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt 1.725 1.725) (pt 1.725 -1.725) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt 1.725 -1.725) (pt -1.725 -1.725) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt -1.725 -1.725) (pt -1.725 1.725) (width 0.2))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt -2.725 2.725) (pt 2.725 2.725) (width 0.1))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt 2.725 2.725) (pt 2.725 -2.725) (width 0.1))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt 2.725 -2.725) (pt -2.725 -2.725) (width 0.1))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt -2.725 -2.725) (pt -2.725 2.725) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(line (pt 0 2.3) (pt 0 2.3) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(arc (pt 0, 2.25) (radius 0.05) (startAngle 90.0) (sweepAngle 180.0) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(line (pt 0 2.2) (pt 0 2.2) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(arc (pt 0, 2.25) (radius 0.05) (startAngle 270) (sweepAngle 180.0) (width 0.1))
		)
	)
	(symbolDef "SST-10-FR-B130-J730" (originalName "SST-10-FR-B130-J730")

		(pin (pinNum 1) (pt 0 mils 0 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -25 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 2) (pt 0 mils -200 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -225 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
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
	(compDef "SST-10-FR-B130-J730" (originalName "SST-10-FR-B130-J730") (compHeader (numPins 3) (numParts 1) (refDesPrefix LED)
		)
		(compPin "1" (pinName "K") (partNum 1) (symPinNum 1) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "2" (pinName "A") (partNum 1) (symPinNum 2) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "3" (pinName "EP") (partNum 1) (symPinNum 3) (gateEq 0) (pinEq 0) (pinType Unknown))
		(attachedSymbol (partNum 1) (altType Normal) (symbolName "SST-10-FR-B130-J730"))
		(attachedPattern (patternNum 1) (patternName "SST10FRB130J730")
			(numPads 3)
			(padPinMap
				(padNum 1) (compPinRef "1")
				(padNum 2) (compPinRef "2")
				(padNum 3) (compPinRef "3")
			)
		)
		(attr "Manufacturer_Name" "Luminus Devices Inc.")
		(attr "Manufacturer_Part_Number" "SST-10-FR-B130-J730")
		(attr "Mouser Part Number" "")
		(attr "Mouser Price/Stock" "")
		(attr "Arrow Part Number" "")
		(attr "Arrow Price/Stock" "")
		(attr "Description" "High Power LEDs - Single Color 730nm FAR RED 1mm 130 degree lens")
		(attr "<Hyperlink>" "https://download.luminus.com/datasheets/Luminus_SST-10-FR_Datasheet.pdf")
		(attr "<Component Height>" "2.03")
		(attr "<STEP Filename>" "SST-10-FR-B130-J730.stp")
		(attr "<STEP Offsets>" "X=0;Y=0;Z=0")
		(attr "<STEP Rotation>" "X=0;Y=0;Z=0")
	)

)
