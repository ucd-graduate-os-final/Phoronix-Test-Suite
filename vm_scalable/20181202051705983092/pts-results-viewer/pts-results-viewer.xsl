<?xml version="1.0" encoding="UTF-8"?>
<!--

Phoronix Test Suite
URLs: http://www.phoronix.com, http://www.phoronix-test-suite.com/
Copyright (C) 2008 - 2014, Phoronix Media
Copyright (C) 2008 - 2014, Michael Larabel

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:template match="/">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title><xsl:value-of select="PhoronixTestSuite/Generated/Title" /> - <xsl:value-of select="PhoronixTestSuite/Generated/TestClient" /> - Results</title>
		<link href="../pts-results-viewer/phoronix-test-suite.css" rel="stylesheet" type="text/css" />
		<link rel="shortcut icon" href="../pts-results-viewer/favicon.ico" />
		<script src="../pts-results-viewer/pts.js" type="text/javascript"></script>
	</head>
	<body>
		<div id="pts_container">
		<div style="overflow: hidden;">
		<div style="text-align: right; float: right; clear: right; margin: 12px 10px 6px 8px;"><a href="http://www.phoronix-test-suite.com/" id="pts_top_logo"></a></div>
		<script type="text/javascript">
		if(navigator.userAgent.indexOf("Konqueror") >= 0)
		{
			document.write("<p style='text-align: center;'>Konqueror generally fails to render the SVG/XSL properly. Please use an alternative web-browser for viewing these results.</p>");
		}
		</script>
		<h1><xsl:value-of select="PhoronixTestSuite/Generated/Title" /></h1>
		<p style="color: #757575;"><xsl:value-of select="PhoronixTestSuite/Generated/Description"/></p>
		<p style="color: #757575;"><em>Generated by <xsl:value-of select="PhoronixTestSuite/Generated/TestClient" /> on <xsl:value-of select="PhoronixTestSuite/Generated/LastModified" />.</em></p>
		</div>
		<div id="pts_banner_nav"><a href="#system_info">System Information</a> <a href="#result-overview">Results Overview</a> <a href="#test-results">Test Results</a> <a href="system-logs/">System Logs</a> <a href="test-logs/">Test Logs</a></div>

		<a name="system_info"></a><h1>System Information</h1>
		<div align="center" style="width: 100%; overflow: auto;"><object type="image/svg+xml"><xsl:attribute name="width">auto</xsl:attribute><xsl:attribute name="height">auto</xsl:attribute><xsl:attribute name="data">result-graphs/systems.svg</xsl:attribute></object></div>
		<div align="center" style="width: 100%; overflow: auto;"><object type="image/svg+xml"><xsl:attribute name="width">auto</xsl:attribute><xsl:attribute name="height">auto</xsl:attribute><xsl:attribute name="data">result-graphs/detailed_component.svg</xsl:attribute></object></div>

		<a name="result-overview"></a><h1>Results Overview</h1>
		<div align="center" style="width: 100%; overflow: auto;"><object type="image/svg+xml"><xsl:attribute name="width">auto</xsl:attribute><xsl:attribute name="height">auto</xsl:attribute><xsl:attribute name="data">result-graphs/radar.svg</xsl:attribute></object></div>
		<div align="center" style="width: 100%; margin-top: 20px; overflow: auto;"><object type="image/svg+xml"><xsl:attribute name="width">auto</xsl:attribute><xsl:attribute name="height">auto</xsl:attribute><xsl:attribute name="data">result-graphs/overview.svg</xsl:attribute></object></div>
		<div align="center" style="width: 100%; margin-top: 20px; overflow: auto;"><object type="image/svg+xml"><xsl:attribute name="width">auto</xsl:attribute><xsl:attribute name="height">auto</xsl:attribute><xsl:attribute name="data">result-graphs/visualize.svg</xsl:attribute></object></div>

		<a name="test-results"></a><h1>Test Results</h1>
		<div id="pts_benchmark_area">
			<xsl:for-each select="PhoronixTestSuite/Result">
				<xsl:variable name="this_test_pos" select="position()" />
				<div class="pts_benchmark_bar"><div style="float: left;"><a><xsl:attribute name="name">test-<xsl:value-of select="$this_test_pos" /></xsl:attribute></a><a><xsl:attribute name="name">b-<xsl:value-of select="$this_test_pos" /></xsl:attribute></a><span class="pts_benchmark_bar_header"><xsl:value-of select="Title"/></span> <span class="pts_benchmark_bar_version"><xsl:value-of select="AppVersion"/></span><br /><strong><xsl:value-of select="ArgumentsDescription"/></strong></div><div style="float: right;"><a style="text-decoration: none;"><xsl:attribute name="href">test-logs/<xsl:value-of select="$this_test_pos" />/</xsl:attribute>View Test Logs</a></div></div>
				<div class="pts_benchmark_img_area"><object type="image/svg+xml"><xsl:attribute name="width">auto</xsl:attribute><xsl:attribute name="height">auto</xsl:attribute><xsl:attribute name="data">result-graphs/<xsl:number value="position()" />.svg</xsl:attribute></object></div>
			</xsl:for-each>
		</div>

		<div id="pts_footer">
			<div id="pts_footer_logo"><a href="http://www.phoronix-test-suite.com/"></a></div>
			<p>Copyright &#xA9; 2008 - 2014 by <a href="http://www.phoronix-media.com/">Phoronix Media</a>.</p>
			<p>All trademarks used are properties of their respective owners. All rights reserved.</p>
		</div>
		</div>

	</body>
</html>
</xsl:template>
</xsl:stylesheet>
