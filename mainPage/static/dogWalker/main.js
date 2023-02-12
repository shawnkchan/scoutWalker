var markers = []; //List to contain all markers added by the user

function initMap() {

    // function showPosition(position) {
    //     let latt = position.coords.latitude,
    //     lngg = position.coords.longitude;
    //     return [latt,lngg];
    // } 
    // navigator.geolocation.getCurrentPosition(showPosition);
    // //callback function: a function whose output gets parsed to the function within its argument. The function within the output uses the output as its own argument.
    // const [latt, lngg] = showPosition();
    // console.log(showPosition());
    const userLoc = { lat: 1.3823023606456615, lng: 103.77730211551497}; 

    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 11,
        center: userLoc,
    });
    
    const marker = new google.maps.Marker({
        position: userLoc,
        map: map,
    });

    infoWindow = new google.maps.InfoWindow();
    const locationButton = document.createElement('button');
    locationButton.textContent = 'Snap to current location';
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
    locationButton.addEventListener('click', ()=> {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const pos = {
                        lat: position.coords.latitude,
                        lng: position.coords.longitude,
                    };

                    infoWindow.setPosition(pos);
                    infoWindow.setContent('Your Location');
                    infoWindow.open(map);
                    map.setCenter(pos);
                },
                () => {
                    handleLocationError(true, infoWindow, map.getCenter());
                }
            );
        } else {
            handleLocationError(false, infoWindow, map.getCenter());
        }
    });

    
    map.addListener('click', (pos) => {
        console.log('clicked');
        placeMarker(pos.latLng, map);
        console.log(markers);
    });
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(
      browserHasGeolocation
        ? "Error: The Geolocation service failed."
        : "Error: Your browser doesn't support geolocation."
    );
    infoWindow.open(map);
  }

//Enable users to place markers and store the coordinates
function placeMarker(latLng, map) {
    var marker = new google.maps.Marker({
        position: latLng,
        map: map,
    });
    map.panTo(latLng);
    markers.push(marker);

    google.maps.event.addListener(marker, 'click', function() {
    this.setMap(null);
  });
}


document.addEventListener('DOMContentLoaded', function(){
    //buttons to toggle the views
    document.querySelector('#profile').addEventListener('click', () => viewProfile());
    document.querySelector('#create').addEventListener('click', () => createRoute());
    document.querySelector('#discover').addEventListener('click', () => viewAllRoutes());
    document.querySelector('#myRoutes').addEventListener('click', () => loadPage('myRoutes-view'));
    //default view to display
    createRoute();
    
    
    
});


function createRoute() {
    document.querySelector('#create-view').style.display ='block';
    document.querySelector('#profile-view').style.display = 'none';
    document.querySelector('#browse-view').style.display = 'none';
    document.querySelector('#myRoutes-view').style.display = 'none';



}


function viewRoute() {

}

function viewAllRoutes() {
    document.querySelector('#create-view').style.display ='none';
    document.querySelector('#profile-view').style.display = 'none';
    document.querySelector('#browse-view').style.display = 'block';
    document.querySelector('#myRoutes-view').style.display = 'none';

    fetch('http://127.0.0.1:8000/discover') 
    .then(response => response.json())
    .then(result => {
        result.forEach(function(route) {
            console.log(route);
        });
    })
}

function favouriteRoutes() {

}

function unFavouriteRoute() {

}

function viewProfile() {
    document.querySelector('#create-view').style.display ='none';
    document.querySelector('#profile-view').style.display = 'block';
    document.querySelector('#browse-view').style.display = 'none';
    document.querySelector('#myRoutes-view').style.display = 'none';
}

function upVote() {

}

function comment() {

}

