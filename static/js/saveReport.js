async function saveReport(){
	var pdf = new jsPDF('p','px', 'letter')
	pdf.setFontSize(10)
	pdf.text("Reporte de rendimiento IOGYM",10,30)


	var date = new Date()
	var today = date.getDate() + "/" + (date.getMonth()+1) + "/" + date.getFullYear()


	var generalDOM = document.getElementById('report-general')

	await domtoimage.toPng(generalDOM)
	.then(function (dataUrl) {
		pdf.text(today, 400, 30)
		pdf.addImage(dataUrl, 'PNG', 30, 40, 400,282);
	})
	.catch(function (error) {
		console.error('oops, something went wrong!', error);
	});


	pdf.addPage()

	var clientsDOM = document.getElementById('report-client')

	await domtoimage.toPng(clientsDOM)
	.then(function (dataUrl) {
		pdf.addImage(dataUrl, 'PNG', 30, 30, 400,388);
	})
	.catch(function (error) {
		console.error('oops, something went wrong!', error);
	});


	pdf.addPage()
	var cflymDOM = document.getElementById('report-clientsByMonth')

	await domtoimage.toPng(cflymDOM)
	.then(function (dataUrl) {
		pdf.addImage(dataUrl, 'PNG', 30, 30, 400,388);
	})
	.catch(function (error) {
		console.error('oops, something went wrong!', error);
	});




	pdf.addPage()
	var nclymDOM = document.getElementById('report-new-clients')

	await domtoimage.toPng(nclymDOM)
	.then(function (dataUrl) {
		pdf.addImage(dataUrl, 'PNG', 30, 30, 400,388);
	})
	.catch(function (error) {
		console.error('oops, something went wrong!', error);
	});



	pdf.save("test.pdf")




};

function convertToCanvas(id){
	canvas = document.getElementById(id);
	return canvas.toDataURL("image/png")
}
