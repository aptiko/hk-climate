all:
	#rst2odt --no-create-sections --odf-config-file=styles.ini --stylesheet-path=styles.odt climate.txt climate.odt
	#rst2html climate.txt climate.html
	r2w climate.ini -w
	r2w climate-el.ini -w
