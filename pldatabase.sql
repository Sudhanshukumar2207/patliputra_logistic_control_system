CREATE TABLE `automatic1` (
  `dipo_id` int DEFAULT NULL,
  `dist_id` int DEFAULT NULL,
  `trans_id` int DEFAULT NULL
)
/

insert into automatic1 values(0,0,0)
/

CREATE TABLE `dipo_details` (
  `dipo_id` varchar(20) DEFAULT NULL,
  `pri_name` varchar(150) DEFAULT NULL,
  `ope_name` varchar(50) DEFAULT NULL,
  `man_name` varchar(50) DEFAULT NULL,
  `man_cont` varchar(50) DEFAULT NULL,
  `dipo_cont` varchar(50) DEFAULT NULL,
  `dipo_tel` varchar(50) DEFAULT NULL,
  `state1` varchar(250) DEFAULT NULL,
  `distr` varchar(50) DEFAULT NULL,
  `addr` varchar(50) DEFAULT NULL,
  `gst` varchar(45) DEFAULT NULL,
  `auto` int DEFAULT NULL
)
/

CREATE TABLE `distributor_details` (
  `dist_id` varchar(50) DEFAULT NULL,
  `dist_name` varchar(150) DEFAULT NULL,
  `cont_no` varchar(50) DEFAULT NULL,
  `dipo_name` varchar(150) DEFAULT NULL,
  `addrs` varchar(250) DEFAULT NULL,
  `state1` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `landline_no` varchar(50) DEFAULT NULL,
  `dipo_id` varchar(45) DEFAULT NULL,
  `gst_no` varchar(45) DEFAULT NULL,
  `le_ex` varchar(45) DEFAULT NULL,
  `pin` varchar(45) DEFAULT NULL
) 
/

CREATE TABLE `drv_pay` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `veh_no` varchar(100) DEFAULT NULL,
  `drv_nm` varchar(200) DEFAULT NULL,
  `sal_mot` varchar(100) DEFAULT NULL,
  `pay_amt` varchar(100) DEFAULT NULL,
  `pay_date` date DEFAULT NULL,
  PRIMARY KEY (`sn`)
)
/

CREATE TABLE `pl_sign` (
  `s_n` int NOT NULL AUTO_INCREMENT,
  `U_NAME` varchar(1000) DEFAULT NULL,
  `U_ID` varchar(1000) DEFAULT NULL,
  `P_WORD` varchar(1000) DEFAULT NULL,
  `S_QUESTIONS` varchar(1000) DEFAULT NULL,
  `S_ANSWER` varchar(1000) DEFAULT NULL,
  `R_O_L_E` varchar(1000) DEFAULT NULL,
  `SATU` varchar(1000) DEFAULT NULL,
  `dipo_id` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`s_n`)
)
/

CREATE TABLE `plorder` (
  `lrno` varchar(25) DEFAULT NULL,
  `lrdate` date DEFAULT NULL,
  `dname` varchar(45) DEFAULT NULL,
  `dtown` varchar(45) DEFAULT NULL,
  `tname` varchar(45) DEFAULT NULL,
  `vno` varchar(45) DEFAULT NULL,
  `vtype` varchar(45) DEFAULT NULL,
  `lt` varchar(10) DEFAULT NULL,
  `ino` varchar(500) DEFAULT NULL,
  `ivalue` varchar(45) DEFAULT NULL,
  `idate` varchar(11) DEFAULT NULL,
  `quantity` varchar(45) DEFAULT NULL,
  `weight` varchar(45) DEFAULT NULL,
  `freight` varchar(45) DEFAULT NULL,
  `le` varchar(45) DEFAULT NULL,
  `ta` varchar(45) DEFAULT NULL,
  `aa` varchar(45) DEFAULT NULL,
  `da` varchar(45) DEFAULT NULL,
  `dipo_id` varchar(45) DEFAULT NULL,
  `m_ch` varchar(45) DEFAULT NULL,
  `pd` varchar(100) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL
)
/

CREATE TABLE `plvehicle` (
  `vtype` varchar(20) DEFAULT NULL,
  `vprise` varchar(10) DEFAULT NULL,
  `cname` varchar(25) DEFAULT NULL,
  `lt` varchar(10) DEFAULT NULL,
  `dipo_id` varchar(45) DEFAULT NULL
)
/


CREATE TABLE `transporter_details` (
  `trans_id` varchar(50) DEFAULT NULL,
  `trans_name` varchar(150) DEFAULT NULL,
  `cont_no` varchar(50) DEFAULT NULL,
  `land_no` varchar(50) DEFAULT NULL,
  `prop_name` varchar(150) DEFAULT NULL,
  `addrs` varchar(250) DEFAULT NULL,
  `state1` varchar(50) DEFAULT NULL,
  `distr` varchar(50) DEFAULT NULL,
  `bnk_name` varchar(150) DEFAULT NULL,
  `acchold_name` varchar(150) DEFAULT NULL,
  `acc_no` varchar(50) DEFAULT NULL,
  `ifsc` varchar(50) DEFAULT NULL,
  `veh_ty` varchar(50) DEFAULT NULL,
  `dipo_id` varchar(45) DEFAULT NULL
) 
/

CREATE TABLE `veh_exp` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `veh_no` varchar(100) DEFAULT NULL,
  `fuel_ty` varchar(100) DEFAULT NULL,
  `fuel_qty` varchar(100) DEFAULT NULL,
  `fuel_amt` varchar(100) DEFAULT NULL,
  `toll_amt` varchar(100) DEFAULT NULL,
  `misc_amt` varchar(100) DEFAULT NULL,
  `tot_amt` varchar(100) DEFAULT NULL,
  `exp_date` date DEFAULT NULL,
  PRIMARY KEY (`sn`)
) 
/

CREATE TABLE `veh_rep` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `veh_no` varchar(100) DEFAULT NULL,
  `veh_part` varchar(500) DEFAULT NULL,
  `rep_prc` varchar(100) DEFAULT NULL,
  `rep_date` date DEFAULT NULL,
  PRIMARY KEY (`sn`)
) 
/



create table state1(
    stat varchar(50),
    distr varchar(6500)
)
/

insert into state1 values('Bihar','Araria,Arwal,Aurangabad,Banka,Begusarai,Bhagalpur,Bhojpur,Buxar,Darbhanga,East Champaran(Motihari),Gaya,Gopalganj,Jamui,Jehanabad,Kaimur(Bhabua),Katihar,Khagaria,Kishanganj,Lakhisarai,Madhepura,Madhubani,Munger(Monghyr),Muzaffarpur,Nalanda,Nawada,Patna,Purnia(Purnea),Rohtas,Saharsa,Samastipur,Saran,Sheikhpura,Sheohar,Sitamarhi,Siwan,Supaul,Vaishali,West Champaran(Bettiah)');

insert into state1 values('Uttar Pradesh','Agra,Aligarh,Allahabad,Ambedkar Nagar,Amethi,Amroha,Auraiya,Azamgarh,Baghpat,Bahraich,Ballia,Balrampur,Banda,Barabanki,Bareilly,Basti,Bhadohi,Bijnor,Budaun,Bulandshahr,Chandauli,Chitrakoot,Deoria,Etah,Etawah,Faizabad,Farrukhabad,Fatehpur,Firozabad,Gautam Buddha Nagar (Noida),Ghaziabad,,Ghazipur,Gonda,Gorakhpur,Hamirpur,Hapur (Panchsheel Nagar),Hardoi,Hathras,Jalaun,Jaunpur,Jhansi,Kannauj,Kanpur Dehat,Kanpur Nagar,Kasganj,Kaushambi,Kushinagar,Lakhimpur Kheri,Lalitpur,Lucknow,Maharajganj,Mahoba,Mainpuri,Mathura,Mau,Meerut,Mirzapur,Moradabad,Muzaffarnagar,Pilibhit,Pratapgarh,Raebareli,Rampur,Saharanpur,Sambhal,Sant Kabir Nagar,Sant Ravidas Nagar (Bhadohi),Shahjahanpur,Shamli,Shravasti,Siddharthnagar,Sitapur,Sonbhadra,Sultanpur,Unnao');

insert into state1 values('Andhra Pradesh','Anantapur,Chittoor,East Godavari,Guntur,Krishna,Kurnool,Nellore,Prakasam,Srikakulam,Visakhapatnam,Vizianagaram,West Godavari,Kadapa (YSR)');

insert into state1 values('Arunachal Pradesh','Tawang,West Kameng,East Kameng,Papumpare,Kurung Kumey,Kra Daadi,Lower Subansiri,Upper Subansiri,West Siang,East Siang,Siang,Upper Siang,Dibang Valley,Lower Dibang Valley,Lohit,Namsai,Anjaw,Changlang,Tirap,Longding');

insert into state1 values('Assam','Baksa,Barpeta,Biswanath,Bongaigaon,Cachar,Charaideo,Chirang,Darrang,Dhemaji,Dhubri,Dibrugarh,Dima Hasao,Goalpara,Golaghat,Hailakandi,Hojai,Jorhat,Kamrup,Kamrup Metropolitan,Karbi Anglong,Karimganj,Kokrajhar,Lakhimpur,Majuli,Morigaon,Nagaon,Nalbari,Dima Hasao,Sivasagar,Sonitpur,South Salamara-Mankachar,Tinsukia,Udalguri,West Karbi Anglong');

insert into state1 values('Chattisgarh','Balod,Baloda Bazar,Balrampur,Bastar,Bemetara,Bijapur,Bilaspur,Dantewada,Dhamtari,Durg,Gariaband,Janjgir-Champa,Jashpur,Kanker,Kabirdham,Korba,Kondagaon,Mahasamund,Mungeli,Narayanpur,Raigarh,Raipur,Rajnandgaon,Sukma,Surajpur,Surguja');

insert into state1 values('Delhi','Central Delhi,East Delhi,New Delhi,North Delhi,North East Delhi,North West Delhi,Shahdara,South Delhi,South East Delhi,South West Delhi,West Delhi');

insert into state1 values('Goa','North Goa,South Goa');

insert into state1 values('Andaman & Nicobar','Nicobar district,North and Middle Andaman district,South Andaman district');

insert into state1 values('Gujarat','Ahmedabad,Amreli,Anand,Aravalli,Banaskantha (Palanpur),Bharuch,Bhavnagar,Botad,Chhota Udepur,Dahod,Dangs (Ahwa),Devbhoomi Dwarka,Gandhinagar,Gir Somnath,Jamnagar,Junagadh,Kheda (Nadiad),Kutch (Bhuj),Mahisagar (Lunavada),Mehsana,Morbi,Narmada (Rajpipla),Navsari,Panchmahal (Godhra),Patan,Porbandar,Rajkot,Sabarkantha (Himmatnagar),Surat,Surendranagar,Tapi (Vyara),Vadodara,Valsad');

insert into state1 values('Haryana','Ambala,Bhiwani,Charkhi Dadri,Faridabad,Fatehabad,Gurugram (Gurgaon),Hisar,Jhajjar,Jind,Kaithal,Karnal,Kurukshetra,Mahendragarh,Nuh,Palwal,Panchkula,Panipat,Rewari,Rohtak,Sirsa,Sonipat,Yamunanagar');

insert into state1 values('Himachal Pradesh','Bilaspur,Chamba,Hamirpur,Kangra,Kinnaur,Kullu,Lahaul and Spiti.Mandi,Shimla,Sirmaur,Solan,Una');

insert into state1 values('Jammu & Kashmir','Anantnag,Bandipora,Baramulla,Budgam,Doda,Ganderbal,Jammu,Kathua,Kishtwar,Kulgam,Kupwara,Leh,Poonch,Pulwama,Rajouri,Ramban,Reasi,Samba,Shopian,Srinagar');

insert into state1 values('Jharkhand','Bokaro,Chatra,Deoghar,Dhanbad,Dumka,East Singhbhum (Jamshedpur),Garhwa,Giridih,Godda,Gumla,Hazaribagh,Jamtara,Khunti,Koderma,Latehar,Lohardaga,Pakur,Palamu,Ramgarh,Ranchi,Sahibganj,Seraikela-Kharsawan,Simdega,West Singhbhum (Chaibasa)');

insert into state1 values('Karnataka','Bagalkot,Ballari (Bellary),Belagavi (Belgaum),Bengaluru (Bangalore) Rural,Bengaluru (Bangalore) Urban,Bidar,Chamarajanagar,Chikballapur,Chikkamagaluru (Chikmagalur),Chitradurga,Dakshina Kannada,Davangere,Dharwad,Gadag,Hassan,Haveri,Kalaburagi (Gulbarga),Kodagu,Kolar,Koppal,Mandya,Mysuru (Mysore),Raichur,Ramanagara,Shivamogga (Shimoga),Tumakuru (Tumkur),Udupi,Uttara Kannada (Karwar),Vijayapura (Bijapur),Yadgir');

insert into state1 values('Kerala','Alappuzha,Ernakulam,Idukki,Kannur,Kasaragod,Kollam,Kottayam,Kozhikode,Malappuram,Palakkad,Pathanamthitta,Thiruvananthapuram,Thrissur,Wayanad');

insert into state1 values('Lakshadweep','Lakshadweep');

insert into state1 values('Madhya Pradesh','Agar Malwa,Alirajpur,Anuppur,Ashoknagar,Balaghat,Barwani,Betul,Bhind,Bhopal,Burhanpur,Chhatarpur,Chhindwara,Damoh,Datia,Dewas,Dhar,Guna,Gwalior,Harda,Hoshangabad,Indore,Jabalpur,Katni,Khandwa,Khargone,Mandla,Mandsaur,Morena,Narsinghpur,Narayanpur,Neemuch,Panna,Raisen,Rajgarh,Ratlam,Rewa,Sagar,Satna,Sehore,Seoni,Shahdol,Shajapur,Sheopur,Shivpuri,Sidhi,Singrauli,Tikamgarh,Ujjain,Umaria,Vidisha');

insert into state1 values('Maharashtra','Ahmednagar,Akola,Amravati,Aurangabad,Beed,Bhandara,Buldhana,Chandrapur,Dhule,Gadchiroli,Gondia,Hingoli,Jalgaon,Jalna,Kolhapur,Latur,Mumbai,Nagpur,Nanded,Nandurbar,Nashik,Osmanabad,Palghar,Parbhani,Pune,Raigad,Ratnagiri,Sangli,Satara,Sindhudurg,Solapur,Thane,Wardha,Washim,Yavatmal');

insert into state1 values('Manipur','Bishnupur,Chandel,Churachandpur,Imphal East,Imphal West,Jiribam,Kakching,Kamjong,Kangpokpi,Noney,Pherzawl,Senapati,Tamenglong,Tengnoupal,Thoubal,Ukhrul');

insert into state1 values('Meghalaya','East Garo Hills,West Garo Hills,South Garo Hills,North Garo Hills,South West Garo Hills,East Khasi Hills,West Khasi Hills,South West Khasi Hills,Ri Bhoi,East Jaintia Hills,West Jaintia Hills');

insert into state1 values('Mizoram','Aizawl,Champhai,Kolasib,Lawngtlai,Lunglei,Mamit,Saiha,Serchhip');

insert into state1 values('Nagaland','Dimapur,Kiphire,Kohima,Longleng,Mokokchung,Mon,Peren,Phek,Tuensang,Wokha,Zunheboto');

insert into state1 values('Odisha','Angul,Balangir,Balasore,Bargarh,Bhadrak,Boudh,Cuttack,Deogarh,Dhenkanal,Gajapati,Ganjam,Jagatsinghpur,Jajpur,Jharsuguda,Kalahandi,Kandhamal,Kendrapara,Kendujhar (Keonjhar),Khordha,Koraput,Malkangiri,Mayurbhanj,Nabarangpur,Nayagarh,Nuapada,Puri,Rayagada,Sambalpur,Sonepur,Sundargarh');

insert into state1 values('Punjab','Amritsar,Barnala,Bathinda,Faridkot,Fatehgarh Sahib,Fazilka,Ferozepur,Gurdaspur,Hoshiarpur,Jalandhar,Kapurthala,Ludhiana,Mansa,Moga,Muktsar,Nawanshahr (Shahid Bhagat Singh Nagar),Pathankot,Patiala,Rupnagar,Sahibzada Ajit Singh Nagar (Mohali),Sangrur,Tarn Taran');

insert into state1 values('Rajasthan','Ajmer,Alwar,Banswara,Baran,Barmer,Bharatpur,Bhilwara,Bikaner,Bundi,Chittorgarh,Churu,Dausa,Dholpur,Dungarpur,Hanumangarh,Jaipur,,Jaisalmer,Jalore,Jhalawar,Jhunjhunu,,,Jodhpur,Karauli,Kota,Nagaur,Pali,Pratapgarh,Rajsamand,Sawai Madhopur,Sikar,Sirohi,Sri Ganganagar,Tonk,Udaipur');

insert into state1 values('Sikkim','East Sikkim,North Sikkim,South Sikkim,West Sikkim');

insert into state1 values('Tamil Nadu','Ariyalur,Chennai,Coimbatore,Cuddalore,Dharmapuri,Dindigul,Erode,Kanchipuram,Kanyakumari,Karur,Krishnagiri,Madurai,Nagapattinam,Namakkal,Nilgiris,Perambalur,Pudukkottai,Ramanathapuram,Salem,Sivaganga,Thanjavur,Theni,Thoothukudi (Tuticorin),Tiruchirappalli (Trichy),Tirunelveli,Tirupathur,Tiruppur,Tiruvallur,Tiruvannamalai,Tiruvarur,Vellore,Viluppuram,Virudhunagar');

insert into state1 values('Telangana','Adilabad,Bhadradri Kothagudem,Hyderabad,Jagitial,Jangaon,Jayashankar Bhupalpally,Jogulamba Gadwal,Kamareddy,Karimnagar,Khammam,Komaram Bheem Asifabad,Mahabubabad,Mahabubnagar,Mancherial,Medak,Medchal-Malkajgiri,Mulugu,Nagarkurnool,Nalgonda,Narayanpet,Nirmal,Nizamabad,Peddapalli,Rajanna Sircilla,Ranga Reddy,Sangareddy,Siddipet,Suryapet,Vikarabad,Wanaparthy,Warangal Rural,Warangal Urban,Yadadri Bhuvanagiri');

insert into state1 values('Tripura','Dhalai,Gomati,Khowai,North Tripura,Sepahijala,South Tripura,Unakoti,West Tripura');

insert into state1 values('Uttarakhand','Almora,Bageshwar,Chamoli,Champawat,Dehradun,Haridwar,Nainital,Pauri Garhwal,Pithoragarh,Rudraprayag,Tehri Garhwal,Udham Singh Nagar,Uttarkashi');

insert into state1 values('West Bengal','Alipurduar,Bankura,Birbhum,Cooch Behar,Dakshin Dinajpur (South Dinajpur),Darjeeling,Hooghly,Howrah,Jalpaiguri,Jhargram,Kalimpong,Kolkata (formerly Calcutta),Malda,Murshidabad,Nadia,North 24 Parganas,Paschim Bardhaman (West Bardhaman),Paschim Medinipur (West Medinipur),Purba Bardhaman (East Bardhaman),Purba Medinipur (East Medinipur),Purulia,South 24 Parganas,Uttar Dinajpur (North Dinajpur)');

insert into state1 values('Chandigarh','Lakshadweep');

insert into state1 values('Dadra & Nagar Haveli and Daman & Diu','Dadra and Nagar Haveli and Daman,Diu');

insert into state1 values('Pondicherry','Karaikal,Mahe,Pondicherry,Yanam');