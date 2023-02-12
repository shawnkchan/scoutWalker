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