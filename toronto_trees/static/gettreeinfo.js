
var map, layer, info;
var vector = new OpenLayers.Layer.Vector('vector');
var style = {
    fillColor: '#000',
    fillOpacity: 0.1,
    strokeWidth: 0
};
var apiKey = "AhjCmC4ThYrtk-3i-01G6buMsQBPOi0SfZO6CCOyhbd1XTHSkI1T_00AZiCBL1HV";
function init(){
  var geographic = new OpenLayers.Projection("EPSG:4326");
  var mercator = new OpenLayers.Projection("EPSG:900913");


  map = new OpenLayers.Map( 'map',{projection: mercator} );
  map.addControl(new OpenLayers.Control.LayerSwitcher());



// 
OpenLayers.Layer.MapQuestOSM = OpenLayers.Class(OpenLayers.Layer.XYZ, {
  name: "MapQuestOSM",
        //attribution: "Data CC-By-SA by <a href='http://openstreetmap.org/'>OpenStreetMap</a>",
        sphericalMercator: true,
        url: 'http://otile1.mqcdn.com/tiles/1.0.0/osm/${z}/${x}/${y}.png',
        
        clone: function(obj) {
          if (obj == null) {
            obj = new OpenLayers.Layer.OSM(
              this.name, this.url, this.getOptions());
          }
          obj = OpenLayers.Layer.XYZ.prototype.clone.apply(this, [obj]);
          return obj;
        },
        CLASS_NAME: "OpenLayers.Layer.MapQuestOSM"
      });



var mapquestosm = new OpenLayers.Layer.MapQuestOSM();    
map.addLayers([mapquestosm]);

//bing satellite layer

var aerial = new OpenLayers.Layer.Bing({
  name: "Aerial",
  key: apiKey,
  type: "Aerial"
});

map.addLayers([aerial]);
// 
layer = new OpenLayers.Layer.WMS("Trees", "http://127.0.0.1:8080/geoserver/cite/wms",
 {layers: 'toronto_trees',transparent: true, tiled: true},
 {isBaseLayer: false}); 
map.addLayer(layer);


map.setCenter(new OpenLayers.LonLat(-79.3836,43.6525).transform(geographic,mercator), 15); 




OpenLayers.Control.ListenToClick = OpenLayers.Class(OpenLayers.Control, {
  defaultHandlerOptions: {
    'single': true,
    'pixelTolerance': 0,
    'stopSingle': false
  },

  initialize: function(options) {
    this.handlerOptions = OpenLayers.Util.extend(
      {}, this.defaultHandlerOptions
      );
    OpenLayers.Control.prototype.initialize.apply(
      this, arguments
      ); 
    this.handler = new OpenLayers.Handler.Click(
      this, {
        'click': this.onClick,
      }, this.handlerOptions
      );
  }, 



  onClick: function (e) {
    var url =  layer.getFullRequestString({
      REQUEST: "GetFeatureInfo",
      EXCEPTIONS: "application/vnd.ogc.se_xml",
      BBOX: layer.map.getExtent().toBBOX(),
      X: e.xy.x,
      Y: e.xy.y,
      INFO_FORMAT: 'text/html',
      QUERY_LAYERS: layer.params.LAYERS,
      WIDTH: layer.map.size.w,
      FEATURE_COUNT: 10,
      HEIGHT: layer.map.size.h});


    if (url) {
      document.getElementById('info').innerHTML =
      '<iframe seamless src="' + url + '" scrolling="no" align="middle"  frameBorder="0" height=100%></iframe>';
    }
    // url.activate();
  },



});
var ctmControl = new OpenLayers.Control.ListenToClick({
  handlerOptions: {
    'single': true,
    'pixelTolerance': 0,
    'stopSingle': false
  }
});
map.addControl(ctmControl);
ctmControl.activate();

map.addLayers([vector]);
var pulsate = function(feature) {
    var point = feature.geometry.getCentroid(),
        bounds = feature.geometry.getBounds(),
        radius = Math.abs((bounds.right - bounds.left)/2),
        count = 0,
        grow = 'up';

    var resize = function(){
        if (count>16) {
            clearInterval(window.resizeInterval);
        }
        var interval = radius * 0.03;
        var ratio = interval/radius;
        switch(count) {
            case 4:
            case 12:
                grow = 'down'; break;
            case 8:
                grow = 'up'; break;
        }
        if (grow!=='up') {
            ratio = - Math.abs(ratio);
        }
        feature.geometry.resize(1+ratio, point);
        vector.drawFeature(feature);
        count++;
    };
    window.resizeInterval = window.setInterval(resize, 50, point, radius);
};

var geolocate = new OpenLayers.Control.Geolocate({
    bind: false,
    geolocationOptions: {
        enableHighAccuracy: false,
        maximumAge: 0,
        timeout: 7000
    }
});
map.addControl(geolocate);
var firstGeolocation = true;
geolocate.events.register("locationupdated",geolocate,function(e) {
    vector.removeAllFeatures();
    var circle = new OpenLayers.Feature.Vector(
        OpenLayers.Geometry.Polygon.createRegularPolygon(
            new OpenLayers.Geometry.Point(e.point.x, e.point.y),
            e.position.coords.accuracy/2,
            40,
            0
        ),
        {},
        style
    );
    vector.addFeatures([
        new OpenLayers.Feature.Vector(
            e.point,
            {},
            {
                graphicName: 'circle',
                strokeColor: '#f00',
                strokeWidth: 2,
                fillOpacity: 0,
                pointRadius: 5
            }
        ),
        circle
    ]);
    if (firstGeolocation) {
        map.zoomToExtent(vector.getDataExtent());
        pulsate(circle);
        firstGeolocation = false;
        this.bind = true;
    }
});
geolocate.events.register("locationfailed",this,function() {
    OpenLayers.Console.log('Location detection failed');
});
document.getElementById('locate').onclick = function() {
    vector.removeAllFeatures();
    geolocate.deactivate();
    geolocate.watch = false;
    firstGeolocation = true;
    geolocate.activate();
};
// document.getElementById('track').onclick = function() {
//     vector.removeAllFeatures();
//     geolocate.deactivate();
//     if (this.checked) {
//         geolocate.watch = true;
//         firstGeolocation = true;
//         geolocate.activate();
//     }
// };
// document.getElementById('track').checked = false;

}