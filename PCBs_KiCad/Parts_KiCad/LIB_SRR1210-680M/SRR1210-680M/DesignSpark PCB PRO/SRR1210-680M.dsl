SamacSys ECAD Model
804809/310146/2.50/2/4/Inductor

DESIGNSPARK_INTERMEDIATE_ASCII

(asciiHeader
	(fileUnits MM)
)
(library Library_1
	(padStyleDef "r530_280"
		(holeDiam 0)
		(padShape (layerNumRef 1) (padShapeType Rect)  (shapeWidth 2.8) (shapeHeight 5.3))
		(padShape (layerNumRef 16) (padShapeType Ellipse)  (shapeWidth 0) (shapeHeight 0))
	)
	(textStyleDef "Default"
		(font
			(fontType Stroke)
			(fontFace "Helvetica")
			(fontHeight 50 mils)
			(strokeWidth 5 mils)
		)
	)
	(patternDef "SRR1210" (originalName "SRR1210")
		(multiLayer
			(pad (padNum 1) (padStyleRef r530_280) (pt 0, -5.1) (rotation 90))
			(pad (padNum 2) (padStyleRef r530_280) (pt 0, 5.1) (rotation 90))
		)
		(layerContents (layerNumRef 18)
			(attr "RefDes" "RefDes" (pt -0.30317, 0.05647) (textStyleRef "Default") (isVisible True))
		)
		(layerContents (layerNumRef 28)
			(line (pt -6 6) (pt 6 6) (width 0.2))
		)
		(layerContents (layerNumRef 28)
			(line (pt 6 6) (pt 6 -6) (width 0.2))
		)
		(layerContents (layerNumRef 28)
			(line (pt 6 -6) (pt -6 -6) (width 0.2))
		)
		(layerContents (layerNumRef 28)
			(line (pt -6 -6) (pt -6 6) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt -6 -6) (pt -6 6) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt 6 6) (pt 6 -6) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt 6 6) (pt 3 6) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt -6 6) (pt -3 6) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt 6 -6) (pt 3 -6) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt -6 -6) (pt -3 -6) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(arc (pt -0.044, -7.101) (radius 0.09289) (startAngle 0.0) (sweepAngle 0.0) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(arc (pt -0.044, -7.101) (radius 0.09289) (startAngle 180.0) (sweepAngle 180.0) (width 0.2))
		)
	)
	(symbolDef "SRR1210-680M" (originalName "SRR1210-680M")

		(pin (pinNum 1) (pt 0 mils 0 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName false)) (pinName (text (pt 0 mils -35 mils) (rotation 0]) (justify "UpperLeft") (textStyleRef "Default"))
		))
		(pin (pinNum 2) (pt 800 mils 0 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName false)) (pinName (text (pt 800 mils -35 mils) (rotation 0]) (justify "UpperRight") (textStyleRef "Default"))
		))
		(arc (pt 250 mils -2 mils) (radius 50 mils) (startAngle 177.7) (sweepAngle -175.4) (width 6 mils))
		(arc (pt 350 mils -2 mils) (radius 50 mils) (startAngle 177.7) (sweepAngle -175.4) (width 6 mils))
		(arc (pt 450 mils -2 mils) (radius 50 mils) (startAngle 177.7) (sweepAngle -175.4) (width 6 mils))
		(arc (pt 550 mils -2 mils) (radius 50 mils) (startAngle 177.7) (sweepAngle -175.4) (width 6 mils))
		(attr "RefDes" "RefDes" (pt 650 mils 250 mils) (justify Left) (isVisible True) (textStyleRef "Default"))

	)
	(compDef "SRR1210-680M" (originalName "SRR1210-680M") (compHeader (numPins 2) (numParts 1) (refDesPrefix L)
		)
		(compPin "1" (pinName "1") (partNum 1) (symPinNum 1) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "2" (pinName "2") (partNum 1) (symPinNum 2) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(attachedSymbol (partNum 1) (altType Normal) (symbolName "SRR1210-680M"))
		(attachedPattern (patternNum 1) (patternName "SRR1210")
			(numPads 2)
			(padPinMap
				(padNum 1) (compPinRef "1")
				(padNum 2) (compPinRef "2")
			)
		)
		(attr "Manufacturer_Name" "Bourns")
		(attr "Manufacturer_Part_Number" "SRR1210-680M")
		(attr "Mouser Part Number" "652-SRR1210-680M")
		(attr "Mouser Price/Stock" "https://www.mouser.co.uk/ProductDetail/Bourns/SRR1210-680M?qs=4vvWAaIu%2Fq7jxuGAr15C2Q%3D%3D")
		(attr "Arrow Part Number" "SRR1210-680M")
		(attr "Arrow Price/Stock" "https://www.arrow.com/en/products/srr1210-680m/bourns")
		(attr "Description" "Power inductor SMD shielded 68uH 3A Bourns SRR1210 Series Shielded Wire-wound SMD Inductor with a Ferrite Core, 68 uH +/-20% 3A Idc Q:12")
		(attr "Datasheet Link" "https://www.bourns.com/pdfs/SRR1210.pdf")
	)

)