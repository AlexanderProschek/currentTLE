const env = require('dotenv').config();
const axios = require('axios');

var req = [];
var flag = true;
while(flag) {
    var add = process.env['SAT'+req.length];
    if(!add) flag = false;
    else {
        req.push(add);
    }
}

console.log(req);

if(req.length == 0) {
    process.exit();
}

req.forEach(async e => {
    try {
        const url = 'https://www.space-track.org/basicspacedata/query/class/tle_latest/ORDINAL/1/NORAD_CAT_ID/'+e;
        const response = await axios.get(url);
        console.log(e);
        console.log(response);
        console.log(response['TLE_LINE2']+'\n');
        } catch (error) {
        console.error(error);
        }
});
