function populateBranches() {
        const districtSelect = document.getElementById('district');
        const branchSelect = document.getElementById('branch');

        // Define branch options for each district
        const branchOptions = {
            'Choose':['----'],
            'Ernakulam': ['Aluva', 'Edapally','Palarivattom'],
            'Alappuzha': ['Cherthala', 'Thakazhy','Vallikunnam'],
            'Idukki': ['Mankulam','Thodupuzha','Thekkady'],
            'Kannur':['Taliparamba','Payyanur','Panoor'],
            'Kasargod':['Kayyur','kadumeni','cheruvathur'],
            'Kollam':['Chinakkada','Pathanapuram','Irumpupalam'],
            'Kottayam':['Kottayam','lathurprayar','Kidangoor'],
            'Kozhikode':['Chalappuram','Koduvally','Kallai'],
            'Malapppuram':['edevannapara','areekode','manjeri'],
            'Palakkad':['Koduvayur','Melmuri','Mangalam'],
            'Pathanamthitta':['Thiruvalla','Kozhencherri','Kuttur'],
            'Thiruvanathapuram':['Kannanmoola','Aakulam','Vellayambalam'],
            'Thrissur':['Guruvayur','Mannuthy','Naickanal'],
            'Wayanad':['Pallikkunnu','Kaniyambetta','Kalpetta'],


        };

        // Clear the current options
        branchSelect.innerHTML = '';

        // Populate branch options based on selected district
        const selectedDistrict = districtSelect.value;
        const branches = branchOptions[selectedDistrict] || [];

        for (const branch of branches) {
            const option = document.createElement('option');
            option.text = branch;
            branchSelect.add(option);
        }
    }





function submitting() {

      const numberInput = parseInt(document.getElementById('phone').value);
      const zipCode = document.getElementById('zip').value;
      const district = document.getElementById('district').value;
      const ifsc = document.getElementById('ifsc').value;

      const acnumber = document.getElementById('acnumber').value;
      const account_type = document.getElementById('account-type').value;

      const ageInput = document.getElementById('ageInput').value;
      const dobInput = document.getElementById('dobInput').value;

       const currentDate = new Date();
       const dob = new Date(dobInput);
       const age = currentDate.getFullYear() - dob.getFullYear();

       var genderRadios = document.getElementsByName('gender');
            var isChecked = false;

            for (var i = 0; i < genderRadios.length; i++) {
                if (genderRadios[i].checked) {
                    isChecked = true;
                    break;
                }
            }

            if (!isChecked) {
                alert('Please select a gender.');
                return false;
            }

      if (numberInput.toString().length != 10 || !/^\d+$/.test(numberInput)) {
        alert('Enter valid number')

      }
      else if(zipCode.toString().length != 6 || !/^\d+$/.test(zipCode)) {
        alert('Enter valid Zip code')
      }
      else if(ifsc.toString().length != 11) {
        alert('Enter valid IFSC code')
      }
      else if(district === 'Choose' ) {
        alert('Choose any district')

      }
      else if(account_type === 'Choose') {
        alert('Choose Type of account')

      }
      else if (age != ageInput) {
       alert("Age or Date Of Birth is not valid")
      }

      else if (acnumber.toString().length <= 8 || acnumber.toString().length > 12 || !/^\d+$/.test(acnumber) ) {
      alert('Enter a valid account number between 8 and 12 digits');
}

//
//       else if(debit=='' || credit == '' || cheque == '') {
//         alert('Choose any material')
//       }
      else {
        alert('Submit form')
      }


      }






