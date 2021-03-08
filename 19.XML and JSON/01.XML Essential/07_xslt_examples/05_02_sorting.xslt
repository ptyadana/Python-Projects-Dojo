<?xml version="1.0"?> 
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

	<xsl:template match="/">
		<html>
		<head>
			<title>Our Items</title>
            <style>
            body {background-color:#DACFE5; font-family:Arial, Helvetica, sans-serif}
            h1.unavail {color:#8A8A8A}
            h1.soon {color:#000077}
            h1.avail {color:#0D3427}
            img {border:0; margin-left:10px}
            </style>
		</head>
		<body>
			<xsl:for-each select="/items/item">
         
         <!-- if it is attribute, put @ -->
         <xsl:sort select="@available" order="descending"/>
         <!-- <xsl:sort select="type" order="ascending"/> -->

            <xsl:choose>
               <xsl:when test="@available = 'no'">
                  <h1 class="unavail">
                     <img>
                        <xsl:attribute name="src">
                           <xsl:value-of select="photo"/>
                        </xsl:attribute>
                     </img>
                     <xsl:text>Type: </xsl:text>
                     <xsl:value-of select="type"/>
                     <xsl:text>, </xsl:text>
                     <xsl:text>Name: </xsl:text>
                     <xsl:value-of select="name"/>
                  </h1>
               </xsl:when>
               <xsl:when test="@available = 'soon'">
                  <h1 class="soon">
                     <img>
                        <xsl:attribute name="src">
                           <xsl:value-of select="photo"/>
                        </xsl:attribute>
                     </img>
                     <xsl:text>Type: </xsl:text>
                     <xsl:value-of select="type"/>
                     <xsl:text>, </xsl:text>
                     <xsl:text>Name: </xsl:text>
                     <xsl:value-of select="name"/>
                  </h1>
               </xsl:when>
               <xsl:otherwise>
                  <h1 class="avail">
                     <img>
                        <xsl:attribute name="src">
                           <xsl:value-of select="photo"/>
                        </xsl:attribute>
                     </img>
                     <xsl:text>Type: </xsl:text>
                     <xsl:value-of select="type"/>
                     <xsl:text>, </xsl:text>
                     <xsl:text>Name: </xsl:text>
                     <xsl:value-of select="name"/>
                  </h1>
               </xsl:otherwise>
            </xsl:choose>
			</xsl:for-each>
		</body>
		</html>
	</xsl:template>

</xsl:stylesheet>
