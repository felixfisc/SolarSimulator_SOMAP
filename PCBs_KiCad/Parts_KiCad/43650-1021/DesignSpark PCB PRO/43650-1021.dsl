SamacSys ECAD Model
11364780/656946/2.50/12/2/Connector

DESIGNSPARK_INTERMEDIATE_ASCII

(asciiHeader
	(fileUnits MM)
)
(library Library_1
	(padStyleDef "r254_127"
		(holeDiam 0)
		(padShape (layerNumRef 1) (padShapeType Rect)  (shapeWidth 1.27) (shapeHeight 2.54))
		(padShape (layerNumRef 16) (padShapeType Ellipse)  (shapeWidth 0) (shapeHeight 0))
	)
	(padStyleDef "c291_h241"
		(holeDiam 2.41)
		(padShape (layerNumRef 1) (padShapeType Ellipse)  (shapeWidth 2.91) (shapeHeight 2.91))
		(padShape (layerNumRef 16) (padShapeType Ellipse)  (shapeWidth 2.91) (shapeHeight 2.91))
	)
	(textStyleDef "Default"
		(font
			(fontType Stroke)
			(fontFace "Helvetica")
			(fontHeight 50 mils)
			(strokeWidth 5 mils)
		)
	)
	(patternDef "43650-10YY_212223" (originalName "43650-10YY_212223")
		(multiLayer
			(pad (padNum 1) (padStyleRef r254_127) (pt 13.5, 0) (rotation 0))
			(pad (padNum 2) (padStyleRef r254_127) (pt 10.5, 0) (rotation 0))
			(pad (padNum 3) (padStyleRef r254_127) (pt 7.5, 0) (rotation 0))
			(pad (padNum 4) (padStyleRef r254_127) (pt 4.5, 0) (rotation 0))
			(pad (padNum 5) (padStyleRef r254_127) (pt 1.5, 0) (rotation 0))
			(pad (padNum 6) (padStyleRef r254_127) (pt -1.5, 0) (rotation 0))
			(pad (padNum 7) (padStyleRef r254_127) (pt -4.5, 0) (rotation 0))
			(pad (padNum 8) (padStyleRef r254_127) (pt -7.5, 0) (rotation 0))
			(pad (padNum 9) (padStyleRef r254_127) (pt -10.5, 0) (rotation 0))
			(pad (padNum 10) (padStyleRef r254_127) (pt -13.5, 0) (rotation 0))
			(pad (padNum 11) (padStyleRef c291_h241) (pt 15.65, -3.43) (rotation 90))
			(pad (padNum 12) (padStyleRef c291_h241) (pt -15.65, -3.43) (rotation 90))
		)
		(layerContents (layerNumRef 18)
			(attr "RefDes" "RefDes" (pt 0, 0) (textStyleRef "Default") (isVisible True))
		)
		(layerContents (layerNumRef 28)
			(line (pt -16.825 -0.96) (pt 16.825 -0.96) (width 0.127))
		)
		(layerContents (layerNumRef 28)
			(line (pt 16.825 -0.96) (pt 16.825 -6.53) (width 0.127))
		)
		(layerContents (layerNumRef 28)
			(line (pt 16.825 -6.53) (pt -16.825 -6.53) (width 0.127))
		)
		(layerContents (layerNumRef 28)
			(line (pt -16.825 -6.53) (pt -16.825 -0.96) (width 0.127))
		)
		(layerContents (layerNumRef 18)
			(line (pt 16.825 -6.53) (pt -16.825 -6.53) (width 0.127))
		)
		(layerContents (layerNumRef 18)
			(line (pt 17 0.5) (pt 17 -0.5) (width 0.127))
		)
		(layerContents (layerNumRef 18)
			(line (pt 17 -0.5) (pt 16 0) (width 0.127))
		)
		(layerContents (layerNumRef 18)
			(line (pt 16 0) (pt 17 0.5) (width 0.127))
		)
		(layerContents (layerNumRef 28)
			(line (pt 17 0.5) (pt 17 -0.5) (width 0.127))
		)
		(layerContents (layerNumRef 28)
			(line (pt 17 -0.5) (pt 16 0) (width 0.127))
		)
		(layerContents (layerNumRef 28)
			(line (pt 16 0) (pt 17 0.5) (width 0.127))
		)
		(layerContents (layerNumRef 30)
			(line (pt -18.3242 2.4892) (pt 18.3242 2.4892) (width 0.05))
		)
		(layerContents (layerNumRef 30)
			(line (pt 18.3242 2.4892) (pt 18.3242 -7.8) (width 0.05))
		)
		(layerContents (layerNumRef 30)
			(line (pt 18.3242 -7.8) (pt -18.3242 -7.8) (width 0.05))
		)
		(layerContents (layerNumRef 30)
			(line (pt -18.3242 -7.8) (pt -18.3242 2.4892) (width 0.05))
		)
	)
	(symbolDef "43650-1021" (originalName "43650-1021")

		(pin (pinNum 1) (pt 900 mils -900 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 670 mils -925 mils) (rotation 0]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 2) (pt 900 mils -800 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 670 mils -825 mils) (rotation 0]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 3) (pt 900 mils -700 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 670 mils -725 mils) (rotation 0]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 4) (pt 900 mils -600 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 670 mils -625 mils) (rotation 0]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 5) (pt 900 mils -500 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 670 mils -525 mils) (rotation 0]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 6) (pt 900 mils -400 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 670 mils -425 mils) (rotation 0]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 7) (pt 900 mils -300 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 670 mils -325 mils) (rotation 0]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 8) (pt 900 mils -200 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 670 mils -225 mils) (rotation 0]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 9) (pt 900 mils -100 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 670 mils -125 mils) (rotation 0]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 10) (pt 900 mils 0 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 670 mils -25 mils) (rotation 0]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 11) (pt 0 mils -100 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -125 mils) (rotation 0]) (justify "Left") (textStyleRef "Default"))
		))
		(pin (pinNum 12) (pt 0 mils 0 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -25 mils) (rotation 0]) (justify "Left") (textStyleRef "Default"))
		))
		(line (pt 200 mils 100 mils) (pt 700 mils 100 mils) (width 6 mils))
		(line (pt 700 mils 100 mils) (pt 700 mils -1000 mils) (width 6 mils))
		(line (pt 700 mils -1000 mils) (pt 200 mils -1000 mils) (width 6 mils))
		(line (pt 200 mils -1000 mils) (pt 200 mils 100 mils) (width 6 mils))
		(attr "RefDes" "RefDes" (pt 750 mils 300 mils) (justify Left) (isVisible True) (textStyleRef "Default"))

	)
	(compDef "43650-1021" (originalName "43650-1021") (compHeader (numPins 12) (numParts 1) (refDesPrefix J)
		)
		(compPin "1" (pinName "1") (partNum 1) (symPinNum 1) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "2" (pinName "2") (partNum 1) (symPinNum 2) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "3" (pinName "3") (partNum 1) (symPinNum 3) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "4" (pinName "4") (partNum 1) (symPinNum 4) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "5" (pinName "5") (partNum 1) (symPinNum 5) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "6" (pinName "6") (partNum 1) (symPinNum 6) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "7" (pinName "7") (partNum 1) (symPinNum 7) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "8" (pinName "8") (partNum 1) (symPinNum 8) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "9" (pinName "9") (partNum 1) (symPinNum 9) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "10" (pinName "10") (partNum 1) (symPinNum 10) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "11" (pinName "11") (partNum 1) (symPinNum 11) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "12" (pinName "12") (partNum 1) (symPinNum 12) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(attachedSymbol (partNum 1) (altType Normal) (symbolName "43650-1021"))
		(attachedPattern (patternNum 1) (patternName "43650-10YY_212223")
			(numPads 12)
			(padPinMap
				(padNum 1) (compPinRef "1")
				(padNum 2) (compPinRef "2")
				(padNum 3) (compPinRef "3")
				(padNum 4) (compPinRef "4")
				(padNum 5) (compPinRef "5")
				(padNum 6) (compPinRef "6")
				(padNum 7) (compPinRef "7")
				(padNum 8) (compPinRef "8")
				(padNum 9) (compPinRef "9")
				(padNum 10) (compPinRef "10")
				(padNum 11) (compPinRef "11")
				(padNum 12) (compPinRef "12")
			)
		)
		(attr "Manufacturer_Name" "Molex")
		(attr "Manufacturer_Part_Number" "43650-1021")
		(attr "Mouser Part Number" "538-43650-1021")
		(attr "Mouser Price/Stock" "https://www.mouser.co.uk/ProductDetail/Molex/43650-1021?qs=H%2FGT2mb2V7axR10lHWY%252B%2FQ%3D%3D")
		(attr "Arrow Part Number" "")
		(attr "Arrow Price/Stock" "")
		(attr "Description" "Micro-Fit 3.0 Vertical Header, 3.00mm Pitch, Single Row, 10 Circuits, with PCB Press-fit Metal Retention Clip")
		(attr "Datasheet Link" "https://www.molex.com/pdm_docs/sd/436500221_sd.pdf")
		(attr "Height" "9.9 mm")
	)

)