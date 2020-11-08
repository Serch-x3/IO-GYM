async function saveReport(){

	var pdf = new jsPDF('p','px', 'letter')
	pdf.setFontSize(0)
	pdf.text("Reporte de rendimiento IOGYM",10,30)


	var date = new Date()
	var today = date.getDate() + "/" + (date.getMonth()+1) + "/" + date.getFullYear()


	var generalDOM = document.getElementById('report-general')
	height = getHeightSize(generalDOM.offsetWidth, generalDOM.offsetHeight, 400)
	await domtoimage.toPng(generalDOM)
	.then(function (dataUrl) {
		pdf.text(today, 400, 30)

		pdf.addImage(dataUrl, 'PNG', 30, 40, 400, height);
	})
	.catch(function (error) {
		console.error('oops, something went wrong!', error);
	});

	updateProgress(25)

	pdf.addPage()

	var clientsDOM = document.getElementById('report-client')
	height = getHeightSize(clientsDOM.offsetWidth, clientsDOM.offsetHeight, 400)
	await domtoimage.toPng(clientsDOM)
	.then(function (dataUrl) {
		pdf.addImage(dataUrl, 'PNG', 30, 30, 400, height);
	})
	.catch(function (error) {
		console.error('oops, something went wrong!', error);
	});


	updateProgress(40)


	pdf.addPage()
	var cflymDOM = document.getElementById('report-clientsByMonth')
	height = getHeightSize(cflymDOM.offsetWidth, cflymDOM.offsetHeight, 400)
	await domtoimage.toPng(cflymDOM)
	.then(function (dataUrl) {
		pdf.addImage(dataUrl, 'PNG', 30, 30, 400, height);
	})
	.catch(function (error) {
		console.error('oops, something went wrong!', error);
	});

	updateProgress(55)

	//New clients last year chart
	pdf.addPage()
	var nclymDOM = document.getElementById('report-new-clients')
	height = getHeightSize(nclymDOM.offsetWidth, nclymDOM.offsetHeight, 400)
	await domtoimage.toPng(nclymDOM)
	.then(function (dataUrl) {
		pdf.addImage(dataUrl, 'PNG', 30, 30, 400,height);
	})
	.catch(function (error) {
		console.error('oops, something went wrong!', error);
	});


	updateProgress(70)


	//Incomes chart
	pdf.addPage()
	var incomesDOM = document.getElementById('report-incomes')
	height = getHeightSize(incomesDOM.offsetWidth, incomesDOM.offsetHeight, 400)
	await domtoimage.toPng(incomesDOM)
	.then(function (dataUrl) {
		pdf.addImage(dataUrl, 'PNG', 30, 30, 400,height);
	})
	.catch(function (error) {
		console.error('oops, something went wrong!', error);
	});


	updateProgress(85)

	//Sales chart
	pdf.addPage()
	var salesDOM = document.getElementById('report-memberships-sold')
	height = getHeightSize(salesDOM.offsetWidth, salesDOM.offsetHeight, 400)
	await domtoimage.toPng(salesDOM)
	.then(function (dataUrl) {
		pdf.addImage(dataUrl, 'PNG', 30, 30, 400,height);
	})
	.catch(function (error) {
		console.error('oops, something went wrong!', error);
	});


	updateProgress(100)

	pdf.save("reporte.pdf")
	$('#pdfModal').modal('hide')
	$('#finishedModal').modal('show')

};

function getHeightSize(width, height, maxwidth){
	return Math.round(maxwidth/ (width/height))
}


function updateProgress(value){
	progressbar = document.getElementById('progress-bar')
	progressbarLabel = document.getElementById('progress-bar-label')
	progressbar.style.width = value+"%"
	progressbarLabel.innerText = value + "%"
}
