clean:
	find . -type f -name '.DS_Store' -delete
	find . -type f -name '*pyc' -delete
	rm -Rf __pycache__
	rm -f ./_evidence/*png
	rm -f ./_evidence/*log
	

backup:
	find . -type f -name '.DS_Store' -delete
	tar -czvf automation_evidences_`date +%Y%m%d_%H%M%S`.tgz _evidence``
	

