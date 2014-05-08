
var map, layer, info;
function init(){
  var geographic = new OpenLayers.Projection("EPSG:4326");
  var mercator = new OpenLayers.Projection("EPSG:900913");


  map = new OpenLayers.Map( 'map',{projection: mercator} );



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

// 
layer = new OpenLayers.Layer.WMS("Trees", "http://localhost:8080/geoserver/cite/gwc/service/wms",
 {layers: 'cite:treemap_trees',transparent: true, tiled: true,styles: "zoom"},
 {isBaseLayer: false}); 
map.addLayer(layer);

// map.addLayers([
//   make_layer("http://overpass-api.de/api/interpreter?data=[timeout:3];node[natural=tree](bbox);out+skel;(way[natural=tree](bbox);node(w););out+skel;", "green")
//   ]); 



map.setCenter(new OpenLayers.LonLat(-79.3836,43.6525).transform(geographic,mercator), 15); 

map.events.register('click', map, function (e) {
  var url =  layer.getFullRequestString({
    REQUEST: "GetFeatureInfo",
    EXCEPTIONS: "application/vnd.ogc.se_xml",
    BBOX: layer.map.getExtent().toBBOX(),
    X: e.xy.x,
    Y: e.xy.y,
    INFO_FORMAT: 'text/html',
    QUERY_LAYERS: layer.params.LAYERS,
    WIDTH: layer.map.size.w,
    HEIGHT: layer.map.size.h});

  if (url) {
    document.getElementById('info').innerHTML =
    '<iframe seamless src="' + url + '"></iframe>';
  }
});

}