all:
	#rst2odt --no-create-sections --odf-config-file=styles.ini --stylesheet-path=styles.odt climate.txt climate.odt
	#rst2html climate.txt climate.html
	mkdir -p output/static/css
	r2w climate.ini -w
	r2w climate-el.ini -w
	lessc less/hkstyle.less >output/static/css/hkstyle.css
	cp -r input/images output/
