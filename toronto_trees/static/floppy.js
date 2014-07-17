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

// //bing satellite layer

// var aerial = new OpenLayers.Layer.Bing({
//   name: "Aerial",
//   key: apiKey,
//   type: "Aerial"
// });

// map.addLayers([aerial]);
// 
layer = new OpenLayers.Layer.WMS("Trees", "http://localhost:8080/geoserver/cite/wms",
 {layers: 'toronto_trees',transparent: true, tiled: true},
 {isBaseLayer: false}); 
map.addLayer(layer);


map.setCenter(new OpenLayers.LonLat(-79.3836,43.6525).transform(geographic,mercator), 15); 

};

