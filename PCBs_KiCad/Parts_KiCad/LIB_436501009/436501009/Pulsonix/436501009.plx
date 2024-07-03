PULSONIX_LIBRARY_ASCII "SamacSys ECAD Model"
//13846205/1265583/2.50/10/2/Connector

(asciiHeader
	(fileUnits MM)
)
(library Library_1
	(padStyleDef "r292_127"
		(holeDiam 0)
		(padShape (layerNumRef 1) (padShapeType Rect)  (shapeWidth 1.27) (shapeHeight 2.92))
		(padShape (layerNumRef 16) (padShapeType Ellipse)  (shapeWidth 0) (shapeHeight 0))
	)
	(padStyleDef "c241_h241"
		(holeDiam 2.41)
		(padShape (layerNumRef 1) (padShapeType Ellipse)  (shapeWidth 2.41) (shapeHeight 2.41))
		(padShape (layerNumRef 16) (padShapeType Ellipse)  (shapeWidth 2.41) (shapeHeight 2.41))
	)
	(textStyleDef "Normal"
		(font
			(fontType Stroke)
			(fontFace "Helvetica")
			(fontHeight 1.27)
			(strokeWidth 0.127)
		)
	)
	(patternDef "4365010YY_091011" (originalName "4365010YY_091011")
		(multiLayer
			(pad (padNum 1) (padStyleRef r292_127) (pt 13.5, 0) (rotation 0))
			(pad (padNum 2) (padStyleRef r292_127) (pt 10.5, 0) (rotation 0))
			(pad (padNum 3) (padStyleRef r292_127) (pt 7.5, 0) (rotation 0))
			(pad (padNum 4) (padStyleRef r292_127) (pt 4.5, 0) (rotation 0))
			(pad (padNum 5) (padStyleRef r292_127) (pt 1.5, 0) (rotation 0))
			(pad (padNum 6) (padStyleRef r292_127) (pt -1.5, 0) (rotation 0))
			(pad (padNum 7) (padStyleRef r292_127) (pt -4.5, 0) (rotation 0))
			(pad (padNum 8) (padStyleRef r292_127) (pt -7.5, 0) (rotation 0))
			(pad (padNum 9) (padStyleRef r292_127) (pt -10.5, 0) (rotation 0))
			(pad (padNum 10) (padStyleRef r292_127) (pt -13.5, 0) (rotation 0))
			(pad (padNum 11) (padStyleRef c241_h241) (pt 15.65, -5.47) (rotation 90))
			(pad (padNum 12) (padStyleRef c241_h241) (pt -15.65, -5.47) (rotation 90))
		)
		(layerContents (layerNumRef 18)
			(attr "RefDes" "RefDes" (pt 0, 0) (textStyleRef "Normal") (isVisible True))
		)
		(layerContents (layerNumRef 28)
			(line (pt -16.83 0.15) (pt 16.83 0.15) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt 16.83 0.15) (pt 16.83 -9.75) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt 16.83 -9.75) (pt -16.83 -9.75) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt -16.83 -9.75) (pt -16.83 0.15) (width 0.025))
		)
		(layerContents (layerNumRef 18)
			(line (pt 16.83 -9.75) (pt -16.83 -9.75) (width 0.127))
		)
		(layerContents (layerNumRef 18)
			(line (pt 16 1.5) (pt 16 0.5) (width 0.127))
		)
		(layerContents (layerNumRef 18)
			(line (pt 16 0.5) (pt 15 1) (width 0.127))
		)
		(layerContents (layerNumRef 18)
			(line (pt 15 1) (pt 16 1.5) (width 0.127))
		)
		(layerContents (layerNumRef 28)
			(line (pt 16 1.5) (pt 16 0.5) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt 16 0.5) (pt 15 1) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt 15 1) (pt 16 1.5) (width 0.025))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt -18.1 2.6792) (pt 18.1 2.6792) (width 0.05))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt 18.1 2.6792) (pt 18.1 -11.02) (width 0.05))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt 18.1 -11.02) (pt -18.1 -11.02) (width 0.05))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt -18.1 -11.02) (pt -18.1 2.6792) (width 0.05))
		)
	)
	(symbolDef "436501009" (originalName "436501009")

		(pin (pinNum 1) (pt 0 mils -900 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -925 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 2) (pt 0 mils -800 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -825 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 3) (pt 0 mils -700 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -725 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 4) (pt 0 mils -600 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -625 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 5) (pt 0 mils -500 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -525 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 6) (pt 0 mils -400 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -425 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 7) (pt 0 mils -300 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -325 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 8) (pt 0 mils -200 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -225 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 9) (pt 0 mils -100 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -125 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 10) (pt 0 mils 0 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -25 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(line (pt 200 mils 100 mils) (pt 600 mils 100 mils) (width 6 mils))
		(line (pt 600 mils 100 mils) (pt 600 mils -1000 mils) (width 6 mils))
		(line (pt 600 mils -1000 mils) (pt 200 mils -1000 mils) (width 6 mils))
		(line (pt 200 mils -1000 mils) (pt 200 mils 100 mils) (width 6 mils))
		(attr "RefDes" "RefDes" (pt 650 mils 300 mils) (justify Left) (isVisible True) (textStyleRef "Normal"))
		(attr "Type" "Type" (pt 650 mils 200 mils) (justify Left) (isVisible True) (textStyleRef "Normal"))

	)
	(compDef "436501009" (originalName "436501009") (compHeader (numPins 10) (numParts 1) (refDesPrefix J)
		)
		(compPin "1" (pinName "1") (partNum 1) (symPinNum 1) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "2" (pinName "2") (partNum 1) (symPinNum 2) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "3" (pinName "3") (partNum 1) (symPinNum 3) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "4" (pinName "4") (partNum 1) (symPinNum 4) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "5" (pinName "5") (partNum 1) (symPinNum 5) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "6" (pinName "6") (partNum 1) (symPinNum 6) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "7" (pinName "7") (partNum 1) (symPinNum 7) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "8" (pinName "8") (partNum 1) (symPinNum 8) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "9" (pinName "9") (partNum 1) (symPinNum 9) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "10" (pinName "10") (partNum 1) (symPinNum 10) (gateEq 0) (pinEq 0) (pinType Unknown))
		(attachedSymbol (partNum 1) (altType Normal) (symbolName "436501009"))
		(attachedPattern (patternNum 1) (patternName "4365010YY_091011")
			(numPads 10)
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
			)
		)
		(attr "Manufacturer_Name" "Molex")
		(attr "Manufacturer_Part_Number" "436501009")
		(attr "Mouser Part Number" "")
		(attr "Mouser Price/Stock" "")
		(attr "Arrow Part Number" "")
		(attr "Arrow Price/Stock" "")
		(attr "Description" "Micro-Fit 3.0 Right-Angle Header, 3.00mm Pitch, Single Row, 10 Circuits, with PCB Press-fit Metal Retention Clip, Glow-Wire Capable, Black, Tape and Reel")
		(attr "<Hyperlink>" "https://www.molex.com/pdm_docs/sd/436500209_sd.pdf")
		(attr "<Component Height>" "5.57")
		(attr "<STEP Filename>" "436501009.stp")
		(attr "<STEP Offsets>" "X=0;Y=-9.52;Z=0.26")
		(attr "<STEP Rotation>" "X=0;Y=0;Z=0")
	)

)