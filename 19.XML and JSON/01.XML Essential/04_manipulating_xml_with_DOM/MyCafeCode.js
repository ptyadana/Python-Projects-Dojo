var gEntreeCount = 0;

// The initialize function takes two arguments: the IDs of the
// HTML <table> element to populate with data and the XML data
// island to use that supplies the data.
function initialize(idTheTable,idXMLData)
{
	// get a reference to the table to populate
	var oTheTable = document.getElementById(idTheTable);
	
	// if the table already has a TBODY section, remove it
	// because we'll be creating a new one from scratch
	var theTBODY = oTheTable.getElementsByTagName('TBODY');
	if (theTBODY.length > 0)
		oTheTable.removeChild(theTBODY[0]);
		
	// now create the menu's content from the XML data. This function
	// will give us back a brand new TBODY to put into the table
	theTBODY = generateMenuContent(idXMLData);
	
	// add the new TBODY to the table
	oTheTable.appendChild(theTBODY);
}

// Given the ID of an XML data island, create a TBODY tag that has
// all the rows and columns for the different menu items. We literally
// build everything in here - the checkboxes, the table rows, the price
// fields - everything.
function generateMenuContent(idXMLData)
{
	var i=0,j=0;
	// make a new empty TBODY section
	var theTBODYNode = document.createElement('TBODY');
	
	// find the XML data island in the document
	var oXMLDoc = document.getElementById(idXMLData);
	
	// now find each one of the SECTION tags in the XML and process
	// each one of them
	var aMenuSections = oXMLDoc.getElementsByTagName('section');
	for (i=0; i < aMenuSections.length; i++)
	{
		// each <section> tag starts a new Menu section, so create 
		// a table row for the section. The text for the table row comes
		// from the the value of the <section> tag's 'name' attribute
		var sName = aMenuSections.item(i).getAttribute('name');
		var oTR = document.createElement('TR');
		var oTD = document.createElement('TD');
		oTD.setAttribute('colspan','3');
		oTD.appendChild(document.createTextNode(sName));
		oTR.appendChild(oTD);
		theTBODYNode.appendChild(oTR);
		
		// now create each menu item. The child tags of each 
		// <section> tag each represent an individual entree.
		var aEntrees = aMenuSections.item(i).getElementsByTagName('entree');
		for (j=0; j < aEntrees.length; j++)
		{
			oTR = document.createElement('TR');
			// create a custom attribute on the TR tag called "vegetarian"
			// to indicate whether the item is vegetarian or not. This
			// will save us a lot of effort later when we're trying to
			// highlight the vegetarian items.
			if (aEntrees.item(j).getAttribute("vegetarian"))
				oTR.setAttribute("data-veg", "true");
				
			// create the TD for the checkbox
			oTD = document.createElement('TD');
			oTD.setAttribute('align','center');
			var oCB = document.createElement('INPUT');
			oCB.setAttribute('name','item' + gEntreeCount++);
			oCB.setAttribute('type','checkbox');
			oTD.appendChild(oCB);
			oTR.appendChild(oTD);
			
			// create the TD for the item name
			oTD = document.createElement('TD');
			var oItemNode = aEntrees.item(j).getElementsByTagName('item')[0];
			// just copy the item node's text child to the TD
			oTD.appendChild(document.createTextNode(oItemNode.firstChild.data));
			oTR.appendChild(oTD);
			
			// create the TD for the price
			oTD = document.createElement('TD');
			// align the prices to the right so they line up
			// over the decimal point
			oTD.setAttribute('align','right');
			var oPriceNode = aEntrees.item(j).getElementsByTagName('price')[0];
			// just copy the price node's text child to the TD
			oTD.appendChild(document.createTextNode(oPriceNode.firstChild.data));
			oTR.appendChild(oTD);

			// add the row to the table body
			theTBODYNode.appendChild(oTR);
		}
	}
	return theTBODYNode;
}

// returns a number that represents the sum of all the selected menu
// item prices.
function calculateBill(idMenuTable)
{
	var fBillTotal = 0.0;
	var i=0;
	
	// find the table tag
	var oTable = document.getElementById(idMenuTable);
	
	// go through the table and add up the prices of all
	// the selected items. The code takes advantage of the 
	// fact that each checkbox has a corresponding row in
	// the table, and the only INPUT tags are the checkboxes.
	var aCBTags = oTable.getElementsByTagName('INPUT');
	for (i=0; i < aCBTags.length; i++)
	{
		// is this menu item selected? it is if the checkbox is checked
		if (aCBTags[i].checked)
		{
			// get the checkbox' parent table row
			var oTR = getParentTag(aCBTags[i],'TR');
			
			// retrieve the price from the price column, which is the third column in the table
			var oTDPrice = oTR.getElementsByTagName('TD')[2];
			// the first child text node of the column contains the price
			fBillTotal += parseFloat(oTDPrice.firstChild.data);
		}
	}
	// return the price as a decimal number with 2 decimal places
	return Math.round(fBillTotal*100.0)/100.0;
}

// This function either turns on or off the row highlighting for vegetarian
// items (depending on the value of bShowVeg)
function highlightVegetarian(idTable,bShowVeg)
{
	// if bShowVeg is true, then we're highlighting vegetarian
	//	meals, otherwise we're unhighlighting them.
	var i=0;
	var oTable = document.getElementById(idTable);

	var oTBODY = oTable.getElementsByTagName('TBODY')[0];
	var aTRs = oTBODY.getElementsByTagName('TR');
	// walk through each of the table rows and see if it has a 
	// "vegetarian" attribute on it.
	for (i=0; i < aTRs.length; i++)
	{
		if (aTRs[i].getAttribute('data-veg'))
		{
			if (bShowVeg)
				aTRs[i].style.backgroundColor = "lightGreen";
			else
				aTRs[i].style.backgroundColor = "";
		}
	}
}

// Utility function for getting the parent tag of a given tag
// but only of a certain type (i.e. a TR, a TABLE, etc.)
function getParentTag(oNode, sParentType)
{
	var oParent = oNode.parentNode;
	while (oParent)
	{
		if (oParent.nodeName == sParentType)
			return oParent;
		oParent = oParent.parentNode;
	}
	return oParent;
}

