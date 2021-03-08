<?xml version="1.0"?> 

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

	<!-- this XSL stylesheet matches the <JavacoTea> tag in an associated XML
	file and replaces it with the HTML contents of the template. -->
	<xsl:template match="/JavacoTea">
		<html>
		<head>
			<title>New Herbal Tea Available!</title>

			<!-- linked with css -->
			<link rel="stylesheet" href="01_03_simpletransform.css"/>
		</head>
		<body>
			<img src="photos/javaco_tea_logo.gif" />
			<h1>
				<!-- select the text from the matched tag, in this case JavacoTea tag-->
				<xsl:value-of select="text()"/>
			</h1>
		</body>
		</html>
	</xsl:template>

</xsl:stylesheet>
