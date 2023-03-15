<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="EEGAndEyeTracker" version="2.0">
	<nodes>
		<node id="0" name="LSL Input" position="(1512.0, 799.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="ObjectPositionStream" uuid="eba43438-510c-40f0-8ca8-e35c2c31abdf" version="1.5.1" />
		<node id="1" name="LSL Input" position="(-5.0, 153.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="EyeTrackerStream" uuid="f07468b1-0501-4f82-8143-49c6cc9df356" version="1.5.1" />
		<node id="2" name="Select Range" position="(395.0, 253.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Blinking Data" uuid="478b0faf-7c39-4d23-94bd-7f7e5643e14b" version="1.1.0" />
		<node id="3" name="LSL Input" position="(-9.0, 1311.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="EEG" uuid="fbf7cab1-923c-4853-b2c3-8449dd016331" version="1.5.1" />
		<node id="4" name="Time Series Plot" position="(1014.0, 1582.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot" uuid="16841007-9b61-4851-a6a8-b0db09ccdd18" version="1.1.0" />
		<node id="5" name="Dejitter Timestamps" position="(161.0, 1321.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="900a5cab-ea32-4cbc-9b91-ff6b299ac459" version="1.0.0" />
		<node id="6" name="FIR Filter" position="(331.0, 1696.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="4c280301-0808-4812-9b17-042c123a565f" version="1.1.0" />
		<node id="7" name="Remove Unlocalized Channels" position="(531.0, 1596.0)" project_name="NeuroPype" qualified_name="widgets.source_localization.owremoveunlocalizedchannels.OWRemoveUnlocalizedChannels" title="Remove Unlocalized Channels" uuid="54ad9cb7-2874-40f9-a832-5c6d13676e0c" version="1.2.0" />
		<node id="8" name="Bad Channel Removal" position="(653.0, 1729.0)" project_name="NeuroPype" qualified_name="widgets.neural.owbadchannelremoval.OWBadChannelRemoval" title="Bad Channel Removal" uuid="31ffaa61-9eda-45af-bbcd-b288c8f49864" version="1.1.2" />
		<node id="9" name="Artifact Removal" position="(783.0, 1725.0)" project_name="NeuroPype" qualified_name="widgets.neural.owartifactremoval.OWArtifactRemoval" title="Artifact Removal" uuid="9fe7e70c-47d8-421f-8645-d11246a8ffc1" version="2.4.1" />
		<node id="10" name="Interpolate Missing Channels" position="(914.0, 1582.0)" project_name="NeuroPype" qualified_name="widgets.neural.owinterpolatemissingchannels.OWInterpolateMissingChannels" title="Interpolate Missing Channels" uuid="039933b2-bd33-4140-a351-5f2c51e0dc44" version="1.4.0" />
		<node id="11" name="Time Series Plot" position="(636.0, 1485.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot (1)" uuid="85f96820-1682-4e83-8de0-773062e1fe4e" version="1.1.0" />
		<node id="12" name="Assign Channel Locations" position="(446.0, 1680.0)" project_name="NeuroPype" qualified_name="widgets.source_localization.owassignchannellocations.OWAssignChannelLocations" title="Assign Channel Locations" uuid="e7d9e9cf-38eb-4977-b484-995126ac323d" version="1.1.0" />
		<node id="13" name="Extract Channel Names" position="(670.0, 1584.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owextractchannels.OWExtractChannels" title="Extract Channel Names" uuid="258d187a-5c8b-4cf3-bf12-e19644ecdd93" version="1.0.1" />
		<node id="14" name="Merge Streams" position="(474.0, 476.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams" uuid="ca45cf73-1e2e-442d-8bd6-e5fac2a66d9d" version="1.0.0" />
		<node id="15" name="Fuse Streams" position="(642.0, 488.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams" uuid="1b805f41-cbae-4840-b50f-460c57759f30" version="0.9.6" />
		<node id="16" name="Record to XDF" position="(122.0, 290.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF" uuid="de2d2d7b-2ab8-4b5c-adf0-10e901bd55f3" version="1.4.0" />
		<node id="17" name="Record to XDF" position="(813.0, 477.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (3)" uuid="70e7a9c8-c3ce-42f4-9a6e-1eb983170c9c" version="1.4.0" />
		<node id="18" name="Record to XDF" position="(129.0, 1454.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (1)" uuid="40c74b01-75b1-45ef-bba5-44aaf6cd0305" version="1.4.0" />
		<node id="19" name="Record to XDF" position="(1737.0, 923.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (2)" uuid="d6d858e0-ef09-45e7-aed4-fcec4c9b7f82" version="1.4.0" />
		<node id="20" name="Time Series Plot" position="(623.0, 183.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot (2)" uuid="780f59e3-764c-40f2-81e0-3c7add1df552" version="1.1.0" />
		<node id="21" name="Add Event Marker" position="(926.0, 317.0)" project_name="NeuroPype" qualified_name="widgets.markers.owaddeventmarker.OWAddEventMarker" title="Add Event Marker" uuid="bbe70f69-7ca9-4665-bb6f-0c6d7c891fd8" version="1.1.0" />
		<node id="22" name="Marker Stream Window" position="(1078.0, 324.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owmarkerstreamwindow.OWMarkerStreamWindow" title="Marker Stream Window" uuid="e4fe0214-0796-42d8-9c11-6fcdcaf940d6" version="1.1.1" />
		<node id="23" name="Break Structure" position="(1228.0, 324.0)" project_name="NeuroPype" qualified_name="widgets.programming.owbreakstructure.OWBreakStructure" title="Break Structure" uuid="bd65bf21-9825-497c-aee7-4792438c21bd" version="1.0.0" />
		<node id="24" name="Shift Timestamps" position="(268.0, 1254.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owshifttimestamps.OWShiftTimestamps" title="Shift Timestamps" uuid="702c5589-0a83-4b1e-ba6a-d3520a38d7f3" version="1.2.1" />
		<node id="25" name="Inspect Packet" position="(349.0, 106.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectpacket.OWInspectPacket" title="Inspect Packet" uuid="14e84179-8811-42ca-99c8-5b41e4a5d96c" version="3.0.1" />
		<node id="26" name="Dejitter Timestamps" position="(109.0, 160.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps (2)" uuid="42b45f8f-b991-41b5-bf29-a56b72f639f4" version="1.0.0" />
		<node id="27" name="Record to XDF" position="(518.0, 1784.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (4)" uuid="ffcac90e-0fce-4850-b73c-28315a8605c7" version="1.4.0" />
		<node id="28" name="Dejitter Timestamps" position="(1650.0, 793.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps (1)" uuid="9af45682-556a-4e42-9985-3b5bb36c6eef" version="1.0.0" />
		<node id="29" name="Record to XDF" position="(25.0, 1465.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (5)" uuid="cfd7ee67-34e0-457e-abc5-6c0fe2000674" version="1.4.0" />
		<node id="30" name="Merge Streams" position="(497.0, 696.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams (1)" uuid="2709fda6-da36-4012-87b7-b5cf928805a2" version="1.0.0" />
		<node id="31" name="Fuse Streams" position="(621.0, 714.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams (1)" uuid="84683d45-d99d-4f47-9088-a0ed17bf9eae" version="0.9.6" />
		<node id="32" name="Record to XDF" position="(779.0, 708.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (6)" uuid="c7b18e4e-b007-43f8-bd8c-4268f3169842" version="1.4.0" />
		<node id="33" name="Record to XDF" position="(33.0, 286.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (7)" uuid="d41e2c91-fa48-4ce1-81fe-2bc33f607960" version="1.4.0" />
		<node id="34" name="Merge Streams" position="(500.0, 924.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams (2)" uuid="5705c43f-d396-46d7-b653-4470a68fbe2d" version="1.0.0" />
		<node id="35" name="Fuse Streams" position="(645.0, 926.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams (2)" uuid="e3be9f7a-3564-4711-b83a-e0e0b87c59f5" version="0.9.6" />
		<node id="36" name="Record to XDF" position="(789.0, 929.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (8)" uuid="8af05c78-2a4a-44dc-874f-e0d06ee1fda2" version="1.4.0" />
		<node id="37" name="Shift Timestamps" position="(436.0, 1547.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owshifttimestamps.OWShiftTimestamps" title="Shift Timestamps (1)" uuid="3591181e-959a-4fe1-8f06-843d7fb281c4" version="1.2.1" />
		<node id="38" name="Merge Streams" position="(503.0, 1144.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams (3)" uuid="4b30a56a-5a06-4645-92d6-d3d6c4631c1d" version="1.0.0" />
		<node id="39" name="Fuse Streams" position="(636.0, 1127.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams (3)" uuid="2cc5c917-ea12-4d6e-8706-9e47aa7ff6d6" version="0.9.6" />
		<node id="40" name="Record to XDF" position="(794.0, 1134.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (9)" uuid="505782a4-b0ee-4cd9-821f-fb1655095c6e" version="1.4.0" />
		<node id="41" name="IIR Filter" position="(186.0, 1776.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="IIR Filter" uuid="66adcba7-2b2e-456d-9ef0-1c71de2259da" version="1.1.0" />
		<node id="42" name="Record to XDF" position="(819.0, 1324.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (9)" uuid="f2e41597-3424-43d3-8a2d-4f8d75511bfe" version="1.4.0" />
		<node id="43" name="Merge Streams" position="(528.0, 1334.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams (3)" uuid="c1e4e933-fc09-4014-9f18-f7687145e2e1" version="1.0.0" />
		<node id="44" name="Fuse Streams" position="(661.0, 1317.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams (3)" uuid="6edf1d33-6101-421e-a3b2-3dc530cb7e58" version="0.9.6" />
		<node id="45" name="Constant Integer" position="(106.0, 914.0)" project_name="NeuroPype" qualified_name="widgets.programming.owconstantint.OWConstantInt" title="Constant Integer" uuid="07008794-0d04-49d5-9445-e263ec1e7aea" version="1.0.0" />
		<node id="46" name="Constant String" position="(1168.0, 916.0)" project_name="NeuroPype" qualified_name="widgets.programming.owconstantstring.OWConstantString" title="Constant String" uuid="2a82deb2-e576-45d0-b6d4-2149b247aa19" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="7" sink_channel="Desired Channels" sink_node_id="10" source_channel="Channel Names" source_node_id="13" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="15" source_channel="Outdata" source_node_id="14" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="17" source_channel="Data" source_node_id="15" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="20" source_channel="Data" source_node_id="2" />
		<link enabled="false" id="12" sink_channel="Data" sink_node_id="21" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="22" source_channel="Data" source_node_id="21" />
		<link enabled="true" id="14" sink_channel="Data2" sink_node_id="14" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="15" sink_channel="Data" sink_node_id="26" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="16" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="26" />
		<link enabled="true" id="17" sink_channel="Data" sink_node_id="25" source_channel="Data" source_node_id="26" />
		<link enabled="true" id="18" sink_channel="Data1" sink_node_id="14" source_channel="Data" source_node_id="26" />
		<link enabled="true" id="19" sink_channel="Data" sink_node_id="16" source_channel="Data" source_node_id="26" />
		<link enabled="true" id="20" sink_channel="Data" sink_node_id="18" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="21" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="22" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="23" sink_channel="Data" sink_node_id="28" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="24" sink_channel="Data" sink_node_id="19" source_channel="Data" source_node_id="28" />
		<link enabled="true" id="25" sink_channel="Data" sink_node_id="27" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="26" sink_channel="Data" sink_node_id="29" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="27" sink_channel="Data" sink_node_id="32" source_channel="Data" source_node_id="31" />
		<link enabled="true" id="28" sink_channel="Data" sink_node_id="31" source_channel="Outdata" source_node_id="30" />
		<link enabled="true" id="29" sink_channel="Data1" sink_node_id="30" source_channel="Data" source_node_id="26" />
		<link enabled="true" id="30" sink_channel="Data2" sink_node_id="30" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="31" sink_channel="Data" sink_node_id="33" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="32" sink_channel="Data" sink_node_id="24" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="33" sink_channel="Data2" sink_node_id="34" source_channel="Data" source_node_id="24" />
		<link enabled="true" id="34" sink_channel="Data1" sink_node_id="34" source_channel="Data" source_node_id="26" />
		<link enabled="true" id="35" sink_channel="Data" sink_node_id="35" source_channel="Outdata" source_node_id="34" />
		<link enabled="true" id="36" sink_channel="Data" sink_node_id="36" source_channel="Data" source_node_id="35" />
		<link enabled="true" id="37" sink_channel="Data" sink_node_id="37" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="38" sink_channel="Data" sink_node_id="40" source_channel="Data" source_node_id="39" />
		<link enabled="true" id="39" sink_channel="Data" sink_node_id="39" source_channel="Outdata" source_node_id="38" />
		<link enabled="true" id="40" sink_channel="Data1" sink_node_id="38" source_channel="Data" source_node_id="26" />
		<link enabled="true" id="41" sink_channel="Data2" sink_node_id="38" source_channel="Data" source_node_id="37" />
		<link enabled="true" id="42" sink_channel="Data" sink_node_id="41" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="43" sink_channel="Data" sink_node_id="42" source_channel="Data" source_node_id="44" />
		<link enabled="true" id="44" sink_channel="Data" sink_node_id="44" source_channel="Outdata" source_node_id="43" />
		<link enabled="true" id="45" sink_channel="Data2" sink_node_id="43" source_channel="Data" source_node_id="41" />
		<link enabled="true" id="46" sink_channel="Data1" sink_node_id="43" source_channel="Data" source_node_id="26" />
		<link enabled="true" id="47" sink_channel="Output Sampling Rate" sink_node_id="15" source_channel="Data" source_node_id="45" />
		<link enabled="true" id="48" sink_channel="Output Sampling Rate" sink_node_id="31" source_channel="Data" source_node_id="45" />
		<link enabled="true" id="49" sink_channel="Output Sampling Rate" sink_node_id="35" source_channel="Data" source_node_id="45" />
		<link enabled="true" id="50" sink_channel="Output Sampling Rate" sink_node_id="39" source_channel="Data" source_node_id="45" />
		<link enabled="true" id="51" sink_channel="Output Sampling Rate" sink_node_id="44" source_channel="Data" source_node_id="45" />
		<link enabled="true" id="52" sink_channel="Output Root" sink_node_id="17" source_channel="Data" source_node_id="46" />
		<link enabled="true" id="53" sink_channel="Output Root" sink_node_id="32" source_channel="Data" source_node_id="46" />
		<link enabled="true" id="54" sink_channel="Output Root" sink_node_id="36" source_channel="Data" source_node_id="46" />
		<link enabled="true" id="55" sink_channel="Output Root" sink_node_id="40" source_channel="Data" source_node_id="46" />
		<link enabled="true" id="56" sink_channel="Output Root" sink_node_id="42" source_channel="Data" source_node_id="46" />
		<link enabled="true" id="57" sink_channel="Output Root" sink_node_id="16" source_channel="Data" source_node_id="46" />
		<link enabled="true" id="58" sink_channel="Output Root" sink_node_id="33" source_channel="Data" source_node_id="46" />
		<link enabled="true" id="59" sink_channel="Output Root" sink_node_id="27" source_channel="Data" source_node_id="46" />
		<link enabled="true" id="60" sink_channel="Output Root" sink_node_id="18" source_channel="Data" source_node_id="46" />
		<link enabled="true" id="61" sink_channel="Output Root" sink_node_id="29" source_channel="Data" source_node_id="46" />
	</links>
	<annotations>
		<text font-family="Helvetica" font-size="16" id="0" rect="(-116.0, 1217.0, 244.0, 62.0)">LSL stream for EEG and cleaning up data.</text>
		<text font-family="Helvetica" font-size="16" id="1" rect="(1494.0, 677.0, 207.0, 88.0)">LSL stream for when objects are looked at and their position.</text>
		<text font-family="Helvetica" font-size="16" id="2" rect="(-34.0, 61.0, 198.0, 50.0)">LSL stream for eye tracking and blinking.</text>
		<text font-family="Helvetica" font-size="16" id="3" rect="(456.0, 402.0, 368.0, 31.0)">Merging dejittered eye tracking and dejittered EEG</text>
		<text font-family="Helvetica" font-size="16" id="4" rect="(489.0, 616.0, 343.0, 69.0)">Merging dejittered eye tracking and dejittered + FIR filtered EEG</text>
		<text font-family="Helvetica" font-size="16" id="5" rect="(515.0, 831.0, 319.0, 69.0)">Mergiing dejittered eye tracking and dejittered + timestamp shifted EEG
</text>
		<text font-family="Helvetica" font-size="16" id="6" rect="(479.0, 1041.0, 348.0, 69.0)">Mergiing dejittered eye tracking and dejittered + FIR + timestamp shifted EEG</text>
		<text font-family="Helvetica" font-size="16" id="7" rect="(504.0, 1231.0, 348.0, 69.0)">Mergiing dejittered eye tracking and dejittered + IIR butter 4th order, [1,28]</text>
		<text font-family="Helvetica" font-size="16" id="8" rect="(54.0, 818.0, 139.0, 69.0)">Sampling rate for fused streams</text>
		<text font-family="Helvetica" font-size="16" id="9" rect="(1177.0, 810.0, 252.0, 83.0)">String containing root for recordings</text>
	</annotations>
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWA4AAABs
b2NhbGhvc3Rfb25seXEIiVgMAAAAbWFya2VyX3F1ZXJ5cQlYAAAAAHEKWAwAAABtYXhfYmxvY2ts
ZW5xC00ABFgKAAAAbWF4X2J1ZmxlbnEMSx5YDAAAAG1heF9jaHVua2xlbnENSwBYCAAAAG1ldGFk
YXRhcQ59cQ9YDAAAAG5vbWluYWxfcmF0ZXEQWA0AAAAodXNlIGRlZmF1bHQpcRFYCQAAAG9taXRf
ZGVzY3ESiVgPAAAAcHJlYWxsb2NfYnVmZmVycROIWA4AAABwcm9jX2Nsb2Nrc3luY3EUiFgNAAAA
cHJvY19kZWppdHRlcnEViVgPAAAAcHJvY19tb25vdG9uaXplcRaJWA8AAABwcm9jX3RocmVhZHNh
ZmVxF4lYBQAAAHF1ZXJ5cRhYFQAAAG5hbWU9J09iamVjdFBvc2l0aW9uJ3EZWAcAAAByZWNvdmVy
cRqIWBQAAAByZXNvbHZlX21pbmltdW1fdGltZXEbRz/gAAAAAAAAWBMAAABzYXZlZFdpZGdldEdl
b21ldHJ5cRxjc2lwCl91bnBpY2tsZV90eXBlCnEdWAwAAABQeVF0NS5RdENvcmVxHlgKAAAAUUJ5
dGVBcnJheXEfQ0IB2dDLAAMAAAAABqoAAAKQAAAIRAAABYEAAAarAAACvQAACEMAAAWAAAAAAAAA
AAAPAAAABqsAAAK9AAAIQwAABYBxIIVxIYdxIlJxI1gOAAAAc2V0X2JyZWFrcG9pbnRxJIlYDwAA
AHVzZV9zdHJlYW1uYW1lc3EliXUu
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWA4AAABs
b2NhbGhvc3Rfb25seXEIiVgMAAAAbWFya2VyX3F1ZXJ5cQlYAAAAAHEKWAwAAABtYXhfYmxvY2ts
ZW5xC00ABFgKAAAAbWF4X2J1ZmxlbnEMSx5YDAAAAG1heF9jaHVua2xlbnENSwBYCAAAAG1ldGFk
YXRhcQ59cQ9YDAAAAG5vbWluYWxfcmF0ZXEQWA0AAAAodXNlIGRlZmF1bHQpcRFYCQAAAG9taXRf
ZGVzY3ESiVgPAAAAcHJlYWxsb2NfYnVmZmVycROIWA4AAABwcm9jX2Nsb2Nrc3luY3EUiFgNAAAA
cHJvY19kZWppdHRlcnEViVgPAAAAcHJvY19tb25vdG9uaXplcRaJWA8AAABwcm9jX3RocmVhZHNh
ZmVxF4lYBQAAAHF1ZXJ5cRhYEQAAAG5hbWU9J0V5ZVRyYWNrZXIncRlYBwAAAHJlY292ZXJxGohY
FAAAAHJlc29sdmVfbWluaW11bV90aW1lcRtHP+AAAAAAAABYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0
cnlxHGNzaXAKX3VucGlja2xlX3R5cGUKcR1YDAAAAFB5UXQ1LlF0Q29yZXEeWAoAAABRQnl0ZUFy
cmF5cR9DQgHZ0MsAAwAAAAAGqgAAAoMAAAhEAAAFjwAABqsAAAKwAAAIQwAABY4AAAAAAAAAAA8A
AAAGqwAAArAAAAhDAAAFjnEghXEhh3EiUnEjWA4AAABzZXRfYnJlYWtwb2ludHEkiVgPAAAAdXNl
X3N0cmVhbW5hbWVzcSWJdS4=
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWB8AAABhcHBseV90aW1lX3NlbGVjdGlv
bl90b19tYXJrZXJzcQKJWAQAAABheGlzcQNYBQAAAHNwYWNlcQRYCAAAAG1ldGFkYXRhcQV9cQZY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxB2NzaXAKX3VucGlja2xlX3R5cGUKcQhYDAAAAFB5UXQ1
LlF0Q29yZXEJWAoAAABRQnl0ZUFycmF5cQpDQgHZ0MsAAwAAAAAKkQAAApcAAA3FAAAFHQAACpIA
AALEAAANxAAABRwAAAAAAAAAAA8AAAAKkgAAAsQAAA3EAAAFHHELhXEMh3ENUnEOWAkAAABzZWxl
Y3Rpb25xD11xEChYCgAAAGxlZnRfYmxpbmtxEVgNAAAAbGVmdF9vcGVubmVzc3ESWAsAAAByaWdo
dF9ibGlua3ETWA4AAAByaWdodF9vcGVubmVzc3EUWAoAAABib3RoX2JsaW5rcRVlWA4AAABzZXRf
YnJlYWtwb2ludHEWiVgEAAAAdW5pdHEXWAUAAABuYW1lc3EYdS4=
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWA4AAABs
b2NhbGhvc3Rfb25seXEIiVgMAAAAbWFya2VyX3F1ZXJ5cQlYAAAAAHEKWAwAAABtYXhfYmxvY2ts
ZW5xC00ABFgKAAAAbWF4X2J1ZmxlbnEMSx5YDAAAAG1heF9jaHVua2xlbnENSwBYCAAAAG1ldGFk
YXRhcQ59cQ9YDAAAAG5vbWluYWxfcmF0ZXEQWA0AAAAodXNlIGRlZmF1bHQpcRFYCQAAAG9taXRf
ZGVzY3ESiVgPAAAAcHJlYWxsb2NfYnVmZmVycROIWA4AAABwcm9jX2Nsb2Nrc3luY3EUiFgNAAAA
cHJvY19kZWppdHRlcnEViVgPAAAAcHJvY19tb25vdG9uaXplcRaJWA8AAABwcm9jX3RocmVhZHNh
ZmVxF4lYBQAAAHF1ZXJ5cRhYHAAAAG5hbWU9J0xpdmVBbXBTTi0wNTYzMDktMDU1MydxGVgHAAAA
cmVjb3ZlcnEaiFgUAAAAcmVzb2x2ZV9taW5pbXVtX3RpbWVxG0c/4AAAAAAAAFgTAAAAc2F2ZWRX
aWRnZXRHZW9tZXRyeXEcY3NpcApfdW5waWNrbGVfdHlwZQpxHVgMAAAAUHlRdDUuUXRDb3JlcR5Y
CgAAAFFCeXRlQXJyYXlxH0NCAdnQywADAAAAAAaqAAACgwAACEQAAAWPAAAGqwAAArAAAAhDAAAF
jgAAAAAAAAAADwAAAAarAAACsAAACEMAAAWOcSCFcSGHcSJScSNYDgAAAHNldF9icmVha3BvaW50
cSSJWA8AAAB1c2Vfc3RyZWFtbmFtZXNxJYl1Lg==
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiFgQAAAAYXV0b19saW5lX2NvbG9yc3EEiVgJAAAAYXV0b3NjYWxlcQWIWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqJWAkAAABmb250X3NpemVxC0dAJAAAAAAAAFgM
AAAAaW5pdGlhbF9kaW1zcQxdcQ0oTdACTbYDTbwCTfQBZVgKAAAAbGluZV9jb2xvcnEOWAcAAAAj
MDAwMDAwcQ9YCgAAAGxpbmVfd2lkdGhxEEc/6AAAAAAAAFgMAAAAbWFya2VyX2NvbG9ycRFYBwAA
ACNGRjAwMDBxElgMAAAAbWF4X2NoYW5uZWxzcRNLIFgIAAAAbWV0YWRhdGFxFH1xFVgMAAAAbmFu
c19hc196ZXJvcRaJWA4AAABub19jb25jYXRlbmF0ZXEXiVgOAAAAb3ZlcnJpZGVfc3JhdGVxGFgN
AAAAKHVzZSBkZWZhdWx0KXEZWAwAAABwbG90X21hcmtlcnNxGohYCwAAAHBsb3RfbWlubWF4cRuJ
WBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRxjc2lwCl91bnBpY2tsZV90eXBlCnEdWAwAAABQeVF0
NS5RdENvcmVxHlgKAAAAUUJ5dGVBcnJheXEfQ0IB2dDLAAMAAAAABrsAAAImAAAIMwAABesAAAa8
AAACUwAACDIAAAXqAAAAAAAAAAAPAAAABrwAAAJTAAAIMgAABepxIIVxIYdxIlJxI1gFAAAAc2Nh
bGVxJEc/8AAAAAAAAFgOAAAAc2V0X2JyZWFrcG9pbnRxJYlYDAAAAHNob3dfdG9vbGJhcnEmiVgL
AAAAc3RyZWFtX25hbWVxJ1gNAAAAKHVzZSBkZWZhdWx0KXEoWAoAAAB0aW1lX3JhbmdlcSlHQBQA
AAAAAABYBQAAAHRpdGxlcSpYIgAAAFRpbWUgc2VyaWVzIEVFRyBBZnRlciBSZW1vdmFsIHZpZXdx
K1gKAAAAemVyb19jb2xvcnEsWAcAAAAjN0Y3RjdGcS1YCAAAAHplcm9tZWFucS6IdS4=
</properties>
		<properties format="literal" node_id="5">{'force_monotonic': True, 'forget_halftime': 90, 'max_updaterate': 500, 'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'warmup_samples': -1}</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEc/0AAAAAAAAEc/4AAAAAAAAEstSzJlWAgAAABtZXRhZGF0YXEJ
fXEKWA0AAABtaW5pbXVtX3BoYXNlcQuIWAQAAABtb2RlcQxYCAAAAGJhbmRwYXNzcQ1YBQAAAG9y
ZGVycQ5YDQAAACh1c2UgZGVmYXVsdClxD1gTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEQY3NpcApf
dW5waWNrbGVfdHlwZQpxEVgMAAAAUHlRdDUuUXRDb3JlcRJYCgAAAFFCeXRlQXJyYXlxE0NCAdnQ
ywADAAAAAAK1AAACsgAABDkAAAR7AAACtgAAAt8AAAQ4AAAEegAAAAAAAAAADwAAAAK2AAAC3wAA
BDgAAAR6cRSFcRWHcRZScRdYDgAAAHNldF9icmVha3BvaW50cRiJWAoAAABzdG9wX2F0dGVucRlH
QEkAAAAAAAB1Lg==
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBAAAABwcm90ZWN0X2NoYW5uZWxzcQNdcQRYEwAAAHNh
dmVkV2lkZ2V0R2VvbWV0cnlxBWNzaXAKX3VucGlja2xlX3R5cGUKcQZYDAAAAFB5UXQ1LlF0Q29y
ZXEHWAoAAABRQnl0ZUFycmF5cQhDQgHZ0MsAAwAAAAAGogAAA5gAAAhLAAAEeQAABqMAAAPFAAAI
SgAABHgAAAAAAAAAAA8AAAAGowAAA8UAAAhKAAAEeHEJhXEKh3ELUnEMWA4AAABzZXRfYnJlYWtw
b2ludHENiXUu
</properties>
		<properties format="literal" node_id="8">{'calib_seconds': 20, 'coords_override': '(use default)', 'corr_threshold': 0.8, 'ignore_chanlocs': False, 'ignored_quantile': 0.1, 'init_on': [], 'keep_unlocalized_channels': False, 'linenoise_aware': True, 'max_bad_channels': 0.15, 'max_broken_time': 0.4, 'metadata': {}, 'min_corr': 0.5, 'noise_threshold': 4, 'num_samples': 200, 'protect_channels': [], 'rereferenced': False, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'subset_size': 0.15, 'use_clean_window': False, 'window_len': 5, 'window_len_cleanwindow': 0.5, 'window_overlap': 0.66, 'zscore_thresholds': [-3.5, 5]}</properties>
		<properties format="literal" node_id="9">{'a': '(use default)', 'b': '(use default)', 'block_size': '(use default)', 'calib_seconds': 45, 'cutoff': 7.5, 'emit_calib_data': True, 'init_on': [], 'lookahead': '(use default)', 'max_bad_channels': 0.2, 'max_dims': 0, 'max_dropout_fraction': 0.1, 'max_mem': 256, 'metadata': {}, 'min_clean_fraction': 0.25, 'min_required_channels': 2, 'preserve_band': '(use default)', 'riemannian': True, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'stddev_cutoff': 20, 'step_size': 0.2, 'use_clean_window': True, 'use_legacy': True, 'window_len_cleanwindow': 0.5, 'window_length': 0.5, 'window_overlap': 0.66, 'window_overlap_cleanwindow': 0.66, 'zscore_thresholds': [-5, 7]}</properties>
		<properties format="literal" node_id="10">{'additive_noise_scale': 0, 'compute_backend': 'keep', 'desired_channels': '(use default)', 'metadata': {}, 'min_ev': '(use default)', 'mode': 'spherical-spline', 'montage': '', 'montage_type': 'auto', 'precision': 'keep', 'randseed': 12345, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'verbose': False}</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiFgQAAAAYXV0b19saW5lX2NvbG9yc3EEiVgJAAAAYXV0b3NjYWxlcQWIWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqJWAkAAABmb250X3NpemVxC0dAJAAAAAAAAFgM
AAAAaW5pdGlhbF9kaW1zcQxdcQ0oSxRNtgNNvAJN9AFlWAoAAABsaW5lX2NvbG9ycQ5YBwAAACMw
MDAwMDBxD1gKAAAAbGluZV93aWR0aHEQRz/oAAAAAAAAWAwAAABtYXJrZXJfY29sb3JxEVgHAAAA
I0ZGMDAwMHESWAwAAABtYXhfY2hhbm5lbHNxE0sgWAgAAABtZXRhZGF0YXEUfXEVWAwAAABuYW5z
X2FzX3plcm9xFolYDgAAAG5vX2NvbmNhdGVuYXRlcReJWA4AAABvdmVycmlkZV9zcmF0ZXEYWA0A
AAAodXNlIGRlZmF1bHQpcRlYDAAAAHBsb3RfbWFya2Vyc3EaiFgLAAAAcGxvdF9taW5tYXhxG4lY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxHGNzaXAKX3VucGlja2xlX3R5cGUKcR1YDAAAAFB5UXQ1
LlF0Q29yZXEeWAoAAABRQnl0ZUFycmF5cR9DQgHZ0MsAAwAAAAAI5QAAAm8AAApdAAAGNAAACOYA
AAKcAAAKXAAABjMAAAAAAAAAAA8AAAAI5gAAApwAAApcAAAGM3EghXEhh3EiUnEjWAUAAABzY2Fs
ZXEkRz/wAAAAAAAAWA4AAABzZXRfYnJlYWtwb2ludHEliVgMAAAAc2hvd190b29sYmFycSaJWAsA
AABzdHJlYW1fbmFtZXEnWA0AAAAodXNlIGRlZmF1bHQpcShYCgAAAHRpbWVfcmFuZ2VxKUdAFAAA
AAAAAFgFAAAAdGl0bGVxKlgjAAAAVGltZSBzZXJpZXMgRUVHIEJlZm9yZSBSZW1vdmFsIHZpZXdx
K1gKAAAAemVyb19jb2xvcnEsWAcAAAAjN0Y3RjdGcS1YCAAAAHplcm9tZWFucS6IdS4=
</properties>
		<properties format="literal" node_id="12">{'force_override': True, 'metadata': {}, 'montage': '', 'montage_type': 'auto', 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="literal" node_id="13">{'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'stream': '', 'verbose': False}</properties>
		<properties format="pickle" node_id="14">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBEAAAByZXBsYWNlX2lmX2V4aXN0c3EDiVgTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDUuUXRDb3Jl
cQZYCgAAAFFCeXRlQXJyYXlxB0NCAdnQywADAAAAAAbCAAADjAAACCsAAASFAAAGwwAAA7kAAAgq
AAAEhAAAAAAAAAAADwAAAAbDAAADuQAACCoAAASEcQiFcQmHcQpScQtYDgAAAHNldF9icmVha3Bv
aW50cQyJWAcAAABzb3J0aW5ncQ1YBQAAAGlucHV0cQ51Lg==
</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWAwAAABidWZmZXJfZGVsYXlxAUsCWBAAAABkZXNpcmVkX2hlYWRyb29tcQJLBVgIAAAA
bWV0YWRhdGFxA31xBFgMAAAAbWluX2hlYWRyb29tcQVLAlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJy
YXlxCUNCAdnQywADAAAAAAavAAADSAAACD4AAATJAAAGsAAAA3UAAAg9AAAEyAAAAAAAAAAADwAA
AAawAAADdQAACD0AAATIcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAUAAABzcmF0
ZXEPS1BYCwAAAHN0cmVhbV9uYW1lcRBYAwAAAGVlZ3ERWAkAAAB2ZXJib3NpdHlxEksBdS4=
</properties>
		<properties format="pickle" node_id="16">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYIAAAAGRlaml0dGVyZWQtZ2F6ZS1hbmQtYmxpbmtpbmcueGRmcQ1YCAAAAG1ldGFkYXRh
cQ59cQ9YCwAAAG91dHB1dF9yb290cRBYGQAAAEU6L2lkYXR0MjkwMF9ncjkyL0xTTERhdGFxEVga
AAAAcHJlc2VydmVfb3JpZ2luYWxfbWV0YWRhdGFxEolYCwAAAHJldHJpZXZhYmxlcROJWBMAAABz
YXZlZFdpZGdldEdlb21ldHJ5cRRjc2lwCl91bnBpY2tsZV90eXBlCnEVWAwAAABQeVF0NS5RdENv
cmVxFlgKAAAAUUJ5dGVBcnJheXEXQ0IB2dDLAAMAAAAABsMAAAMDAAAIKgAABToAAAbDAAADAwAA
CCoAAAU6AAAAAAAAAAAPAAAABsMAAAMDAAAIKgAABTpxGIVxGYdxGlJxG1gNAAAAc2Vzc2lvbl9u
b3Rlc3EcaAVYDgAAAHNldF9icmVha3BvaW50cR2JWAcAAAB2ZXJib3NlcR6JdS4=
</properties>
		<properties format="pickle" node_id="17">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYLQAAAGRlaml0dGVyZWQtZWVnLWFuZC1kZWppdHRlcmVkLWV5ZXRyYWNraW5nLnhkZnEN
WAgAAABtZXRhZGF0YXEOfXEPWAsAAABvdXRwdXRfcm9vdHEQWBkAAABFOi9pZGF0dDI5MDBfZ3I5
Mi9MU0xEYXRhcRFYGgAAAHByZXNlcnZlX29yaWdpbmFsX21ldGFkYXRhcRKJWAsAAAByZXRyaWV2
YWJsZXETiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEUY3NpcApfdW5waWNrbGVfdHlwZQpxFVgM
AAAAUHlRdDUuUXRDb3JlcRZYCgAAAFFCeXRlQXJyYXlxF0NCAdnQywADAAAAAAaGAAAEFAAACPQA
AAZLAAAGhgAABBQAAAj0AAAGSwAAAAAAAAAADwAAAAaGAAAEFAAACPQAAAZLcRiFcRmHcRpScRtY
DQAAAHNlc3Npb25fbm90ZXNxHGgFWA4AAABzZXRfYnJlYWtwb2ludHEdiVgHAAAAdmVyYm9zZXEe
iXUu
</properties>
		<properties format="pickle" node_id="18">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYEgAAAGRlaml0dGVyZWQtZWVnLnhkZnENWAgAAABtZXRhZGF0YXEOfXEPWAsAAABvdXRw
dXRfcm9vdHEQWBkAAABFOi9pZGF0dDI5MDBfZ3I5Mi9MU0xEYXRhcRFYGgAAAHByZXNlcnZlX29y
aWdpbmFsX21ldGFkYXRhcRKJWAsAAAByZXRyaWV2YWJsZXETiVgTAAAAc2F2ZWRXaWRnZXRHZW9t
ZXRyeXEUY3NpcApfdW5waWNrbGVfdHlwZQpxFVgMAAAAUHlRdDUuUXRDb3JlcRZYCgAAAFFCeXRl
QXJyYXlxF0NCAdnQywADAAAAAAbCAAAC1gAACCsAAAU7AAAGwwAAAwMAAAgqAAAFOgAAAAAAAAAA
DwAAAAbDAAADAwAACCoAAAU6cRiFcRmHcRpScRtYDQAAAHNlc3Npb25fbm90ZXNxHGgFWA4AAABz
ZXRfYnJlYWtwb2ludHEdiVgHAAAAdmVyYm9zZXEeiXUu
</properties>
		<properties format="pickle" node_id="19">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYCwAAAG9iai1wb3MueGRmcQ1YCAAAAG1ldGFkYXRhcQ59cQ9YCwAAAG91dHB1dF9yb290
cRBYGQAAAEU6L2lkYXR0MjkwMF9ncjkyL0xTTERhdGFxEVgaAAAAcHJlc2VydmVfb3JpZ2luYWxf
bWV0YWRhdGFxEolYCwAAAHJldHJpZXZhYmxlcROJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRRj
c2lwCl91bnBpY2tsZV90eXBlCnEVWAwAAABQeVF0NS5RdENvcmVxFlgKAAAAUUJ5dGVBcnJheXEX
Q0IB2dDLAAMAAAAABsMAAAMDAAAIKgAABToAAAbDAAADAwAACCoAAAU6AAAAAAAAAAAPAAAABsMA
AAMDAAAIKgAABTpxGIVxGYdxGlJxG1gNAAAAc2Vzc2lvbl9ub3Rlc3EcaAVYDgAAAHNldF9icmVh
a3BvaW50cR2JWAcAAAB2ZXJib3NlcR6JdS4=
</properties>
		<properties format="pickle" node_id="20">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGIWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiFgQAAAAYXV0b19saW5lX2NvbG9yc3EEiFgJAAAAYXV0b3NjYWxlcQWJWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqJWAkAAABmb250X3NpemVxC0dAJAAAAAAAAFgM
AAAAaW5pdGlhbF9kaW1zcQxdcQ0oSzJLMk28Ak30AWVYCgAAAGxpbmVfY29sb3JxDlgHAAAAIzAw
MDAwMHEPWAoAAABsaW5lX3dpZHRocRBHP+gAAAAAAABYDAAAAG1hcmtlcl9jb2xvcnERWAcAAAAj
RkYwMDAwcRJYDAAAAG1heF9jaGFubmVsc3ETSyBYCAAAAG1ldGFkYXRhcRR9cRVYDAAAAG5hbnNf
YXNfemVyb3EWiFgOAAAAbm9fY29uY2F0ZW5hdGVxF4lYDgAAAG92ZXJyaWRlX3NyYXRlcRhYDQAA
ACh1c2UgZGVmYXVsdClxGVgMAAAAcGxvdF9tYXJrZXJzcRqIWAsAAABwbG90X21pbm1heHEbiVgT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEcY3NpcApfdW5waWNrbGVfdHlwZQpxHVgMAAAAUHlRdDUu
UXRDb3JlcR5YCgAAAFFCeXRlQXJyYXlxH0NCAdnQywADAAAAAAbuAAACMQAACGYAAAX2AAAG7wAA
Al4AAAhlAAAF9QAAAAAAAAAADwAAAAbvAAACXgAACGUAAAX1cSCFcSGHcSJScSNYBQAAAHNjYWxl
cSRHP+gAAAAAAABYDgAAAHNldF9icmVha3BvaW50cSWJWAwAAABzaG93X3Rvb2xiYXJxJolYCwAA
AHN0cmVhbV9uYW1lcSdYDQAAACh1c2UgZGVmYXVsdClxKFgKAAAAdGltZV9yYW5nZXEpR0AkAAAA
AAAAWAUAAAB0aXRsZXEqWBAAAABUaW1lIHNlcmllcyB2aWV3cStYCgAAAHplcm9fY29sb3JxLFgH
AAAAIzdGN0Y3RnEtWAgAAAB6ZXJvbWVhbnEuiXUu
</properties>
		<properties format="pickle" node_id="21">gAN9cQAoWA4AAABldmVudF90b19tYXRjaHEBWAAAAABxAlgWAAAAbWF0Y2hfZmlyc3RfZXZlbnRf
b25seXEDiVgIAAAAbWV0YWRhdGFxBH1xBVgQAAAAbmV3X2V2ZW50X21hcmtlcnEGaAJYEwAAAHNh
dmVkV2lkZ2V0R2VvbWV0cnlxB2NzaXAKX3VucGlja2xlX3R5cGUKcQhYDAAAAFB5UXQ1LlF0Q29y
ZXEJWAoAAABRQnl0ZUFycmF5cQpDQgHZ0MsAAwAAAAAJEQAAAckAAAp/AAADgAAACRIAAAH2AAAK
fgAAA38AAAAAAAAAAA8AAAAJEgAAAfYAAAp+AAADf3ELhXEMh3ENUnEOWA4AAABzZXRfYnJlYWtw
b2ludHEPiVgGAAAAc3RyZWFtcRBoAlgOAAAAdHJpYWxfY3JpdGVyaWFxEV1xElgMAAAAbGVmdF9i
bGluaz0xcRNhWAkAAAB0cmlhbF9lbmRxFGgCWAsAAAB0cmlhbF9zdGFydHEVaAJYBwAAAHZlcmJv
c2VxFol1Lg==
</properties>
		<properties format="literal" node_id="22">{'always_on_top': False, 'initial_dims': [50, 50, 500, 500], 'metadata': {}, 'override_srate': '(use default)', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'stream_name': 'Markers'}</properties>
		<properties format="literal" node_id="23">{'default0': '(use default)', 'default1': '(use default)', 'default10': '(use default)', 'default11': '(use default)', 'default12': '(use default)', 'default13': '(use default)', 'default14': '(use default)', 'default2': '(use default)', 'default3': '(use default)', 'default4': '(use default)', 'default5': '(use default)', 'default6': '(use default)', 'default7': '(use default)', 'default8': '(use default)', 'default9': '(use default)', 'defaults_type': 'str', 'metadata': {}, 'name0': '(use default)', 'name1': '(use default)', 'name10': '(use default)', 'name11': '(use default)', 'name12': '(use default)', 'name13': '(use default)', 'name14': '(use default)', 'name2': '(use default)', 'name3': '(use default)', 'name4': '(use default)', 'name5': '(use default)', 'name6': '(use default)', 'name7': '(use default)', 'name8': '(use default)', 'name9': '(use default)', 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="24">gAN9cQAoWBMAAABiZWdpbm5pbmdfZnJvbV96ZXJvcQGJWBUAAABjb21wZW5zYXRlX2ZpbHRlcl9s
YWdxAolYDwAAAGluY2x1ZGVfbWFya2Vyc3EDiVgNAAAAbWFya2VyX2ZpZWxkc3EEWA0AAAAodXNl
IGRlZmF1bHQpcQVYCAAAAG1ldGFkYXRhcQZ9cQdYBgAAAG9mZnNldHEIR7+7ItDlYEGJWBsAAABv
ZmZzZXRfdHJpZ2dlcnNfc3RhdGVfcmVzZXRxCYhYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxCmNz
aXAKX3VucGlja2xlX3R5cGUKcQtYDAAAAFB5UXQ1LlF0Q29yZXEMWAoAAABRQnl0ZUFycmF5cQ1D
QgHZ0MsAAwAAAAAGcAAAA14AAAfXAAAE2AAABnAAAANeAAAH1wAABNgAAAAAAAAAAA8AAAAGcAAA
A14AAAfXAAAE2HEOhXEPh3EQUnERWA4AAABzZXRfYnJlYWtwb2ludHESiVgPAAAAdGltZXN0YW1w
X3BhaXJzcRNYDQAAACh1c2UgZGVmYXVsdClxFFgNAAAAdXNlX3RpbWVfYXhpc3EViHUu
</properties>
		<properties format="literal" node_id="25">{'always_on_top': True, 'col_axis': 'time', 'decimals': 6, 'every_n_ticks': 1, 'fewer_buttons': False, 'font_size': 10, 'initial_position': [20, 50, 500, 400], 'metadata': {}, 'row_axis': 'space', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'show_axes_table': True, 'show_data_table': True, 'show_markers_table': False, 'show_max_columns': 20, 'show_max_values': 50, 'show_streams_table': False, 'stream_name': '(use default)', 'verbose': True, 'window_title': 'Inspect Data Packet'}</properties>
		<properties format="pickle" node_id="26">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECS1pYDgAA
AG1heF91cGRhdGVyYXRlcQNN9AFYCAAAAG1ldGFkYXRhcQR9cQVYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxBmNzaXAKX3VucGlja2xlX3R5cGUKcQdYDAAAAFB5UXQ1LlF0Q29yZXEIWAoAAABRQnl0
ZUFycmF5cQlDQgHZ0MsAAwAAAAAGqgAAA2sAAAhEAAAEpwAABqsAAAOYAAAIQwAABKYAAAAAAAAA
AA8AAAAGqwAAA5gAAAhDAAAEpnEKhXELh3EMUnENWA4AAABzZXRfYnJlYWtwb2ludHEOiVgOAAAA
d2FybXVwX3NhbXBsZXNxD0r/////dS4=
</properties>
		<properties format="pickle" node_id="27">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYGgAAAGRlaml0dGVyZWQtYW5kLWZpci1lZWcueGRmcQ1YCAAAAG1ldGFkYXRhcQ59cQ9Y
CwAAAG91dHB1dF9yb290cRBYGQAAAEU6L2lkYXR0MjkwMF9ncjkyL0xTTERhdGFxEVgaAAAAcHJl
c2VydmVfb3JpZ2luYWxfbWV0YWRhdGFxEolYCwAAAHJldHJpZXZhYmxlcROJWBMAAABzYXZlZFdp
ZGdldEdlb21ldHJ5cRRjc2lwCl91bnBpY2tsZV90eXBlCnEVWAwAAABQeVF0NS5RdENvcmVxFlgK
AAAAUUJ5dGVBcnJheXEXQ0IB2dDLAAMAAAAABsIAAALWAAAIKwAABTsAAAbDAAADAwAACCoAAAU6
AAAAAAAAAAAPAAAABsMAAAMDAAAIKgAABTpxGIVxGYdxGlJxG1gNAAAAc2Vzc2lvbl9ub3Rlc3Ec
aAVYDgAAAHNldF9icmVha3BvaW50cR2JWAcAAAB2ZXJib3NlcR6JdS4=
</properties>
		<properties format="literal" node_id="28">{'force_monotonic': True, 'forget_halftime': 90, 'max_updaterate': 500, 'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'warmup_samples': -1}</properties>
		<properties format="pickle" node_id="29">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYCwAAAHJhdy1lZWcueGRmcQ1YCAAAAG1ldGFkYXRhcQ59cQ9YCwAAAG91dHB1dF9yb290
cRBYGQAAAEU6L2lkYXR0MjkwMF9ncjkyL0xTTERhdGFxEVgaAAAAcHJlc2VydmVfb3JpZ2luYWxf
bWV0YWRhdGFxEolYCwAAAHJldHJpZXZhYmxlcROJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRRj
c2lwCl91bnBpY2tsZV90eXBlCnEVWAwAAABQeVF0NS5RdENvcmVxFlgKAAAAUUJ5dGVBcnJheXEX
Q0IB2dDLAAMAAAAABsIAAALWAAAIKwAABTsAAAbDAAADAwAACCoAAAU6AAAAAAAAAAAPAAAABsMA
AAMDAAAIKgAABTpxGIVxGYdxGlJxG1gNAAAAc2Vzc2lvbl9ub3Rlc3EcaAVYDgAAAHNldF9icmVh
a3BvaW50cR2JWAcAAAB2ZXJib3NlcR6JdS4=
</properties>
		<properties format="pickle" node_id="30">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBEAAAByZXBsYWNlX2lmX2V4aXN0c3EDiVgTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDUuUXRDb3Jl
cQZYCgAAAFFCeXRlQXJyYXlxB0NCAdnQywADAAAAAAbCAAADjAAACCsAAASFAAAGwwAAA7kAAAgq
AAAEhAAAAAAAAAAADwAAAAbDAAADuQAACCoAAASEcQiFcQmHcQpScQtYDgAAAHNldF9icmVha3Bv
aW50cQyJWAcAAABzb3J0aW5ncQ1YBQAAAGlucHV0cQ51Lg==
</properties>
		<properties format="pickle" node_id="31">gAN9cQAoWAwAAABidWZmZXJfZGVsYXlxAUsCWBAAAABkZXNpcmVkX2hlYWRyb29tcQJLBVgIAAAA
bWV0YWRhdGFxA31xBFgMAAAAbWluX2hlYWRyb29tcQVLAlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJy
YXlxCUNCAdnQywADAAAAAAavAAADSAAACD4AAATJAAAGsAAAA3UAAAg9AAAEyAAAAAAAAAAADwAA
AAawAAADdQAACD0AAATIcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAUAAABzcmF0
ZXEPS1BYCwAAAHN0cmVhbV9uYW1lcRBYAwAAAGVlZ3ERWAkAAAB2ZXJib3NpdHlxEksBdS4=
</properties>
		<properties format="pickle" node_id="32">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYMQAAAGRlaml0dGVyZWQtZmlyLWVlZy1hbmQtZGVqaXR0ZXJlZC1leWV0cmFja2luZy54
ZGZxDVgIAAAAbWV0YWRhdGFxDn1xD1gLAAAAb3V0cHV0X3Jvb3RxEFgZAAAARTovaWRhdHQyOTAw
X2dyOTIvTFNMRGF0YXERWBoAAABwcmVzZXJ2ZV9vcmlnaW5hbF9tZXRhZGF0YXESiVgLAAAAcmV0
cmlldmFibGVxE4lYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxFGNzaXAKX3VucGlja2xlX3R5cGUK
cRVYDAAAAFB5UXQ1LlF0Q29yZXEWWAoAAABRQnl0ZUFycmF5cRdDQgHZ0MsAAwAAAAAGwgAAAtYA
AAjlAAAFOwAABsMAAAMDAAAI5AAABToAAAAAAAAAAA8AAAAGwwAAAwMAAAjkAAAFOnEYhXEZh3Ea
UnEbWA0AAABzZXNzaW9uX25vdGVzcRxoBVgOAAAAc2V0X2JyZWFrcG9pbnRxHYlYBwAAAHZlcmJv
c2VxHol1Lg==
</properties>
		<properties format="pickle" node_id="33">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYFQAAAGdhemUtYW5kLWJsaW5raW5nLnhkZnENWAgAAABtZXRhZGF0YXEOfXEPWAsAAABv
dXRwdXRfcm9vdHEQWBkAAABFOi9pZGF0dDI5MDBfZ3I5Mi9MU0xEYXRhcRFYGgAAAHByZXNlcnZl
X29yaWdpbmFsX21ldGFkYXRhcRKJWAsAAAByZXRyaWV2YWJsZXETiVgTAAAAc2F2ZWRXaWRnZXRH
ZW9tZXRyeXEUY3NpcApfdW5waWNrbGVfdHlwZQpxFVgMAAAAUHlRdDUuUXRDb3JlcRZYCgAAAFFC
eXRlQXJyYXlxF0NCAdnQywADAAAAAAbCAAAC1gAACCsAAAU7AAAGwwAAAwMAAAgqAAAFOgAAAAAA
AAAADwAAAAbDAAADAwAACCoAAAU6cRiFcRmHcRpScRtYDQAAAHNlc3Npb25fbm90ZXNxHGgFWA4A
AABzZXRfYnJlYWtwb2ludHEdiVgHAAAAdmVyYm9zZXEeiXUu
</properties>
		<properties format="literal" node_id="34">{'metadata': {}, 'replace_if_exists': False, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'sorting': 'input'}</properties>
		<properties format="pickle" node_id="35">gAN9cQAoWAwAAABidWZmZXJfZGVsYXlxAUsCWBAAAABkZXNpcmVkX2hlYWRyb29tcQJLBVgIAAAA
bWV0YWRhdGFxA31xBFgMAAAAbWluX2hlYWRyb29tcQVLAlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJy
YXlxCUNCAdnQywADAAAAAAavAAADSAAACD4AAATJAAAGsAAAA3UAAAg9AAAEyAAAAAAAAAAADwAA
AAawAAADdQAACD0AAATIcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAUAAABzcmF0
ZXEPS1BYCwAAAHN0cmVhbV9uYW1lcRBYAwAAAGVlZ3ERWAkAAAB2ZXJib3NpdHlxEksBdS4=
</properties>
		<properties format="pickle" node_id="36">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYRQAAAGRlaml0dGVyZWQtdGltZXN0YW1wLXNoaWZ0ZWQtMTA2bXMtZWVnLWFuZC1kZWpp
dHRlcmVkLWV5ZXRyYWNraW5nLnhkZnENWAgAAABtZXRhZGF0YXEOfXEPWAsAAABvdXRwdXRfcm9v
dHEQWBkAAABFOi9pZGF0dDI5MDBfZ3I5Mi9MU0xEYXRhcRFYGgAAAHByZXNlcnZlX29yaWdpbmFs
X21ldGFkYXRhcRKJWAsAAAByZXRyaWV2YWJsZXETiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEU
Y3NpcApfdW5waWNrbGVfdHlwZQpxFVgMAAAAUHlRdDUuUXRDb3JlcRZYCgAAAFFCeXRlQXJyYXlx
F0NCAdnQywADAAAAAAbCAAAC1gAACSsAAAU7AAAGwwAAAwMAAAkqAAAFOgAAAAAAAAAADwAAAAbD
AAADAwAACSoAAAU6cRiFcRmHcRpScRtYDQAAAHNlc3Npb25fbm90ZXNxHGgFWA4AAABzZXRfYnJl
YWtwb2ludHEdiVgHAAAAdmVyYm9zZXEeiXUu
</properties>
		<properties format="pickle" node_id="37">gAN9cQAoWBMAAABiZWdpbm5pbmdfZnJvbV96ZXJvcQGJWBUAAABjb21wZW5zYXRlX2ZpbHRlcl9s
YWdxAolYDwAAAGluY2x1ZGVfbWFya2Vyc3EDiVgNAAAAbWFya2VyX2ZpZWxkc3EEWA0AAAAodXNl
IGRlZmF1bHQpcQVYCAAAAG1ldGFkYXRhcQZ9cQdYBgAAAG9mZnNldHEIR7+keuFHrhR7WBsAAABv
ZmZzZXRfdHJpZ2dlcnNfc3RhdGVfcmVzZXRxCYhYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxCmNz
aXAKX3VucGlja2xlX3R5cGUKcQtYDAAAAFB5UXQ1LlF0Q29yZXEMWAoAAABRQnl0ZUFycmF5cQ1D
QgHZ0MsAAwAAAAAGwgAAAzUAAAgrAAAE3QAABsMAAANiAAAIKgAABNwAAAAAAAAAAA8AAAAGwwAA
A2IAAAgqAAAE3HEOhXEPh3EQUnERWA4AAABzZXRfYnJlYWtwb2ludHESiVgPAAAAdGltZXN0YW1w
X3BhaXJzcRNoBVgNAAAAdXNlX3RpbWVfYXhpc3EUiXUu
</properties>
		<properties format="pickle" node_id="38">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBEAAAByZXBsYWNlX2lmX2V4aXN0c3EDiVgTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDUuUXRDb3Jl
cQZYCgAAAFFCeXRlQXJyYXlxB0NCAdnQywADAAAAAAbCAAADjAAACCsAAASFAAAGwwAAA7kAAAgq
AAAEhAAAAAAAAAAADwAAAAbDAAADuQAACCoAAASEcQiFcQmHcQpScQtYDgAAAHNldF9icmVha3Bv
aW50cQyJWAcAAABzb3J0aW5ncQ1YBQAAAGlucHV0cQ51Lg==
</properties>
		<properties format="pickle" node_id="39">gAN9cQAoWAwAAABidWZmZXJfZGVsYXlxAUsCWBAAAABkZXNpcmVkX2hlYWRyb29tcQJLBVgIAAAA
bWV0YWRhdGFxA31xBFgMAAAAbWluX2hlYWRyb29tcQVLAlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJy
YXlxCUNCAdnQywADAAAAAAavAAADSAAACD4AAATJAAAGsAAAA3UAAAg9AAAEyAAAAAAAAAAADwAA
AAawAAADdQAACD0AAATIcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAUAAABzcmF0
ZXEPS1BYCwAAAHN0cmVhbV9uYW1lcRBYAwAAAGVlZ3ERWAkAAAB2ZXJib3NpdHlxEksBdS4=
</properties>
		<properties format="pickle" node_id="40">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYSAAAAGRlaml0dGVyZWQtZmlyLXRpbWVzdGFtcC1zaGlmdGVkLTQwbXMtZWVnLWFuZC1k
ZWppdHRlcmVkLWV5ZXRyYWNraW5nLnhkZnENWAgAAABtZXRhZGF0YXEOfXEPWAsAAABvdXRwdXRf
cm9vdHEQWBkAAABFOi9pZGF0dDI5MDBfZ3I5Mi9MU0xEYXRhcRFYGgAAAHByZXNlcnZlX29yaWdp
bmFsX21ldGFkYXRhcRKJWAsAAAByZXRyaWV2YWJsZXETiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEUY3NpcApfdW5waWNrbGVfdHlwZQpxFVgMAAAAUHlRdDUuUXRDb3JlcRZYCgAAAFFCeXRlQXJy
YXlxF0NCAdnQywADAAAAAAbCAAAC1gAACCsAAAU7AAAGwwAAAwMAAAgqAAAFOgAAAAAAAAAADwAA
AAbDAAADAwAACCoAAAU6cRiFcRmHcRpScRtYDQAAAHNlc3Npb25fbm90ZXNxHGgFWA4AAABzZXRf
YnJlYWtwb2ludHEdiVgHAAAAdmVyYm9zZXEeiXUu
</properties>
		<properties format="pickle" node_id="41">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEsBSxxlWAsAAABpZ25vcmVfbmFuc3EHiVgIAAAAbWV0YWRhdGFx
CH1xCVgEAAAAbW9kZXEKWAgAAABiYW5kcGFzc3ELWBAAAABvZmZsaW5lX2ZpbHRmaWx0cQyJWAUA
AABvcmRlcnENSwRYCQAAAHBhc3NfbG9zc3EOR0AIAAAAAAAAWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cQ9jc2lwCl91bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0NS5RdENvcmVxEVgKAAAAUUJ5dGVB
cnJheXESQ0IB2dDLAAMAAAAABasAAAMXAAAHOAAABOUAAAWsAAADRAAABzcAAATkAAAAAAAAAAAP
AAAABawAAANEAAAHNwAABORxE4VxFIdxFVJxFlgOAAAAc2V0X2JyZWFrcG9pbnRxF4lYCgAAAHN0
b3BfYXR0ZW5xGEdASQAAAAAAAHUu
</properties>
		<properties format="pickle" node_id="42">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYMQAAAGRlaml0dGVyZWQtaWlyLWVlZy1hbmQtZGVqaXR0ZXJlZC1leWV0cmFja2luZy54
ZGZxDVgIAAAAbWV0YWRhdGFxDn1xD1gLAAAAb3V0cHV0X3Jvb3RxEFgZAAAARTovaWRhdHQyOTAw
X2dyOTIvTFNMRGF0YXERWBoAAABwcmVzZXJ2ZV9vcmlnaW5hbF9tZXRhZGF0YXESiVgLAAAAcmV0
cmlldmFibGVxE4lYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxFGNzaXAKX3VucGlja2xlX3R5cGUK
cRVYDAAAAFB5UXQ1LlF0Q29yZXEWWAoAAABRQnl0ZUFycmF5cRdDQgHZ0MsAAwAAAAAGwgAAAtYA
AAgrAAAFOwAABsMAAAMDAAAIKgAABToAAAAAAAAAAA8AAAAGwwAAAwMAAAgqAAAFOnEYhXEZh3Ea
UnEbWA0AAABzZXNzaW9uX25vdGVzcRxoBVgOAAAAc2V0X2JyZWFrcG9pbnRxHYlYBwAAAHZlcmJv
c2VxHol1Lg==
</properties>
		<properties format="pickle" node_id="43">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBEAAAByZXBsYWNlX2lmX2V4aXN0c3EDiVgTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDUuUXRDb3Jl
cQZYCgAAAFFCeXRlQXJyYXlxB0NCAdnQywADAAAAAAbCAAADjAAACCsAAASFAAAGwwAAA7kAAAgq
AAAEhAAAAAAAAAAADwAAAAbDAAADuQAACCoAAASEcQiFcQmHcQpScQtYDgAAAHNldF9icmVha3Bv
aW50cQyJWAcAAABzb3J0aW5ncQ1YBQAAAGlucHV0cQ51Lg==
</properties>
		<properties format="pickle" node_id="44">gAN9cQAoWAwAAABidWZmZXJfZGVsYXlxAUsCWBAAAABkZXNpcmVkX2hlYWRyb29tcQJLBVgIAAAA
bWV0YWRhdGFxA31xBFgMAAAAbWluX2hlYWRyb29tcQVLAlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJy
YXlxCUNCAdnQywADAAAAAAawAAADdQAACD0AAATsAAAGsAAAA3UAAAg9AAAE7AAAAAAAAAAADwAA
AAawAAADdQAACD0AAATscQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAUAAABzcmF0
ZXEPS1BYCwAAAHN0cmVhbV9uYW1lcRBYAwAAAGVlZ3ERWAkAAAB2ZXJib3NpdHlxEksBdS4=
</properties>
		<properties format="pickle" node_id="45">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQNjc2lwCl91
bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NS5RdENvcmVxBVgKAAAAUUJ5dGVBcnJheXEGQ0IB2dDL
AAMAAAAABsIAAAOYAAAIKwAABHkAAAbDAAADxQAACCoAAAR4AAAAAAAAAAAPAAAABsMAAAPFAAAI
KgAABHhxB4VxCIdxCVJxClgOAAAAc2V0X2JyZWFrcG9pbnRxC4lYBQAAAHZhbHVlcQxLUHUu
</properties>
		<properties format="pickle" node_id="46">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQNjc2lwCl91
bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NS5RdENvcmVxBVgKAAAAUUJ5dGVBcnJheXEGQ0IB2dDL
AAMAAAAABsIAAAOYAAAIKwAABHkAAAbDAAADxQAACCoAAAR4AAAAAAAAAAAPAAAABsMAAAPFAAAI
KgAABHhxB4VxCIdxCVJxClgOAAAAc2V0X2JyZWFrcG9pbnRxC4lYBQAAAHZhbHVlcQxYGQAAAEU6
L2lkYXR0MjkwMF9ncjkyL0xTTERhdGFxDXUu
</properties>
	</node_properties>
	<patch>{
    "description": {
        "description": "(description missing)",
        "license": "",
        "name": "(untitled)",
        "status": "(unspecified)",
        "url": "",
        "version": "0.0.0"
    },
    "edges": [
        [
            "node9",
            "data",
            "node10",
            "data"
        ],
        [
            "node11",
            "data",
            "node5",
            "data"
        ],
        [
            "node6",
            "data",
            "node7",
            "data"
        ],
        [
            "node6",
            "data",
            "node15",
            "data2"
        ],
        [
            "node6",
            "data",
            "node19",
            "data"
        ],
        [
            "node6",
            "data",
            "node25",
            "data"
        ],
        [
            "node6",
            "data",
            "node42",
            "data"
        ],
        [
            "node8",
            "data",
            "node12",
            "data"
        ],
        [
            "node8",
            "data",
            "node14",
            "data"
        ],
        [
            "node8",
            "data",
            "node9",
            "data"
        ],
        [
            "node7",
            "data",
            "node13",
            "data"
        ],
        [
            "node7",
            "data",
            "node28",
            "data"
        ],
        [
            "node7",
            "data",
            "node31",
            "data2"
        ],
        [
            "node7",
            "data",
            "node38",
            "data"
        ],
        [
            "node13",
            "data",
            "node8",
            "data"
        ],
        [
            "node14",
            "channel_names",
            "node11",
            "desired_channels"
        ],
        [
            "node15",
            "outdata",
            "node16",
            "data"
        ],
        [
            "node16",
            "data",
            "node18",
            "data"
        ],
        [
            "node4",
            "data",
            "node6",
            "data"
        ],
        [
            "node4",
            "data",
            "node30",
            "data"
        ],
        [
            "node3",
            "data",
            "node21",
            "data"
        ],
        [
            "node22",
            "data",
            "node23",
            "data"
        ],
        [
            "node2",
            "data",
            "node27",
            "data"
        ],
        [
            "node2",
            "data",
            "node34",
            "data"
        ],
        [
            "node27",
            "data",
            "node3",
            "data"
        ],
        [
            "node27",
            "data",
            "node26",
            "data"
        ],
        [
            "node27",
            "data",
            "node15",
            "data1"
        ],
        [
            "node27",
            "data",
            "node17",
            "data"
        ],
        [
            "node27",
            "data",
            "node31",
            "data1"
        ],
        [
            "node27",
            "data",
            "node35",
            "data1"
        ],
        [
            "node27",
            "data",
            "node39",
            "data1"
        ],
        [
            "node27",
            "data",
            "node44",
            "data1"
        ],
        [
            "node10",
            "data",
            "node11",
            "data"
        ],
        [
            "node1",
            "data",
            "node29",
            "data"
        ],
        [
            "node29",
            "data",
            "node20",
            "data"
        ],
        [
            "node32",
            "data",
            "node33",
            "data"
        ],
        [
            "node31",
            "outdata",
            "node32",
            "data"
        ],
        [
            "node25",
            "data",
            "node35",
            "data2"
        ],
        [
            "node35",
            "outdata",
            "node36",
            "data"
        ],
        [
            "node36",
            "data",
            "node37",
            "data"
        ],
        [
            "node40",
            "data",
            "node41",
            "data"
        ],
        [
            "node39",
            "outdata",
            "node40",
            "data"
        ],
        [
            "node38",
            "data",
            "node39",
            "data2"
        ],
        [
            "node45",
            "data",
            "node43",
            "data"
        ],
        [
            "node44",
            "outdata",
            "node45",
            "data"
        ],
        [
            "node42",
            "data",
            "node44",
            "data2"
        ],
        [
            "node46",
            "data",
            "node16",
            "srate"
        ],
        [
            "node46",
            "data",
            "node32",
            "srate"
        ],
        [
            "node46",
            "data",
            "node36",
            "srate"
        ],
        [
            "node46",
            "data",
            "node40",
            "srate"
        ],
        [
            "node46",
            "data",
            "node45",
            "srate"
        ],
        [
            "node47",
            "data",
            "node18",
            "output_root"
        ],
        [
            "node47",
            "data",
            "node33",
            "output_root"
        ],
        [
            "node47",
            "data",
            "node37",
            "output_root"
        ],
        [
            "node47",
            "data",
            "node41",
            "output_root"
        ],
        [
            "node47",
            "data",
            "node43",
            "output_root"
        ],
        [
            "node47",
            "data",
            "node17",
            "output_root"
        ],
        [
            "node47",
            "data",
            "node34",
            "output_root"
        ],
        [
            "node47",
            "data",
            "node28",
            "output_root"
        ],
        [
            "node47",
            "data",
            "node19",
            "output_root"
        ],
        [
            "node47",
            "data",
            "node30",
            "output_root"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "exclude_desc_fields": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "localhost_only": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_query": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "omit_desc": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "prealloc_buffer": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_clocksync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_dejitter": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_monotonize": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_threadsafe": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='ObjectPosition'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "eba43438-510c-40f0-8ca8-e35c2c31abdf"
        },
        "node10": {
            "class": "ArtifactRemoval",
            "module": "neuropype.nodes.neural.ArtifactRemoval",
            "params": {
                "a": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "b": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "block_size": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "calib_seconds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 45
                },
                "cutoff": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 7.5
                },
                "emit_calib_data": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "init_on": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "lookahead": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "max_bad_channels": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "max_dims": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0
                },
                "max_dropout_fraction": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.1
                },
                "max_mem": {
                    "customized": false,
                    "type": "Port",
                    "value": 256
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "min_clean_fraction": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.25
                },
                "min_required_channels": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 2
                },
                "preserve_band": {
                    "customized": false,
                    "type": "DictPort",
                    "value": null
                },
                "riemannian": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stddev_cutoff": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 20
                },
                "step_size": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "use_clean_window": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_legacy": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "window_len_cleanwindow": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "window_length": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "window_overlap": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.66
                },
                "window_overlap_cleanwindow": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.66
                },
                "zscore_thresholds": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        -5,
                        7
                    ]
                }
            },
            "uuid": "9fe7e70c-47d8-421f-8645-d11246a8ffc1"
        },
        "node11": {
            "class": "InterpolateMissingChannels",
            "module": "neuropype.nodes.neural.InterpolateMissingChannels",
            "params": {
                "additive_noise_scale": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0
                },
                "compute_backend": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "keep"
                },
                "desired_channels": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "Fp1",
                        "Fz",
                        "F3",
                        "F7",
                        "F9",
                        "FC5",
                        "FC1",
                        "C3",
                        "T7",
                        "CP5",
                        "CP1",
                        "Pz",
                        "P3",
                        "P7",
                        "P9",
                        "O1",
                        "Oz",
                        "O2",
                        "P10",
                        "P8",
                        "P4",
                        "CP2",
                        "CP6",
                        "T8",
                        "C4",
                        "Cz",
                        "FC2",
                        "FC6",
                        "F10",
                        "F8",
                        "F4",
                        "Fp2"
                    ]
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "min_ev": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "spherical-spline"
                },
                "montage": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "montage_type": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "auto"
                },
                "precision": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "keep"
                },
                "randseed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 12345
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "039933b2-bd33-4140-a351-5f2c51e0dc44"
        },
        "node12": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_line_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "font_size": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 10.0
                },
                "initial_dims": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        20,
                        950,
                        700,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "max_channels": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 32
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "no_concatenate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5.0
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Time series EEG Before Removal view"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "85f96820-1682-4e83-8de0-773062e1fe4e"
        },
        "node13": {
            "class": "AssignChannelLocations",
            "module": "neuropype.nodes.source_localization.AssignChannelLocations",
            "params": {
                "force_override": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "montage": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "montage_type": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "auto"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "e7d9e9cf-38eb-4977-b484-995126ac323d"
        },
        "node14": {
            "class": "ExtractChannels",
            "module": "neuropype.nodes.utilities.ExtractChannels",
            "params": {
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "258d187a-5c8b-4cf3-bf12-e19644ecdd93"
        },
        "node15": {
            "class": "MergeStreams",
            "module": "neuropype.nodes.formatting.MergeStreams",
            "params": {
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "replace_if_exists": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "sorting": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "input"
                }
            },
            "uuid": "ca45cf73-1e2e-442d-8bd6-e5fac2a66d9d"
        },
        "node16": {
            "class": "FuseStreams",
            "module": "neuropype.nodes.formatting.FuseStreams",
            "params": {
                "buffer_delay": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 2
                },
                "desired_headroom": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "min_headroom": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 2
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "srate": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 80
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "eeg"
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                }
            },
            "uuid": "1b805f41-cbae-4840-b50f-460c57759f30"
        },
        "node17": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "dejittered-gaze-and-blinking.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "E:/idatt2900_gr92/LSLData"
                },
                "preserve_original_metadata": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "de2d2d7b-2ab8-4b5c-adf0-10e901bd55f3"
        },
        "node18": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "dejittered-eeg-and-dejittered-eyetracking.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "E:/idatt2900_gr92/LSLData"
                },
                "preserve_original_metadata": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "70e7a9c8-c3ce-42f4-9a6e-1eb983170c9c"
        },
        "node19": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "dejittered-eeg.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "E:/idatt2900_gr92/LSLData"
                },
                "preserve_original_metadata": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "40c74b01-75b1-45ef-bba5-44aaf6cd0305"
        },
        "node2": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "exclude_desc_fields": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "localhost_only": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_query": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "omit_desc": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "prealloc_buffer": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_clocksync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_dejitter": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_monotonize": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_threadsafe": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='EyeTracker'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "f07468b1-0501-4f82-8143-49c6cc9df356"
        },
        "node20": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "obj-pos.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "E:/idatt2900_gr92/LSLData"
                },
                "preserve_original_metadata": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "d6d858e0-ef09-45e7-aed4-fcec4c9b7f82"
        },
        "node21": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_line_colors": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "autoscale": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "font_size": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 10.0
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "max_channels": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 32
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nans_as_zero": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "no_concatenate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 10.0
                },
                "title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Time series view"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F"
                },
                "zeromean": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "780f59e3-764c-40f2-81e0-3c7add1df552"
        },
        "node22": {
            "class": "AddEventMarker",
            "module": "neuropype.nodes.markers.AddEventMarker",
            "params": {
                "event_to_match": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "match_first_event_only": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "new_event_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "trial_criteria": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "left_blink=1"
                    ]
                },
                "trial_end": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "trial_start": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "bbe70f69-7ca9-4665-bb6f-0c6d7c891fd8"
        },
        "node23": {
            "class": "MarkerStreamWindow",
            "module": "neuropype.nodes.visualization.MarkerStreamWindow",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        500,
                        500
                    ]
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Markers"
                }
            },
            "uuid": "e4fe0214-0796-42d8-9c11-6fcdcaf940d6"
        },
        "node24": {
            "class": "BreakStructure",
            "module": "neuropype.nodes.programming.BreakStructure",
            "params": {
                "default0": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "default1": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "default10": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "default11": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "default12": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "default13": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "default14": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "default2": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "default3": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "default4": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "default5": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "default6": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "default7": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "default8": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "default9": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "defaults_type": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "str"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "name0": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "name1": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "name10": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "name11": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "name12": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "name13": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "name14": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "name2": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "name3": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "name4": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "name5": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "name6": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "name7": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "name8": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "name9": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "bd65bf21-9825-497c-aee7-4792438c21bd"
        },
        "node25": {
            "class": "ShiftTimestamps",
            "module": "neuropype.nodes.utilities.ShiftTimestamps",
            "params": {
                "beginning_from_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "compensate_filter_lag": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "include_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_fields": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "offset": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": -0.106
                },
                "offset_triggers_state_reset": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "timestamp_pairs": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "use_time_axis": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "702c5589-0a83-4b1e-ba6a-d3520a38d7f3"
        },
        "node26": {
            "class": "InspectPacket",
            "module": "neuropype.nodes.visualization.InspectPacket",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "col_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "decimals": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 6
                },
                "every_n_ticks": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "fewer_buttons": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "font_size": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 10
                },
                "initial_position": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        20,
                        50,
                        500,
                        400
                    ]
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "row_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "space"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_axes_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_data_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_markers_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_max_columns": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 20
                },
                "show_max_values": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 50
                },
                "show_streams_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "window_title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Inspect Data Packet"
                }
            },
            "uuid": "14e84179-8811-42ca-99c8-5b41e4a5d96c"
        },
        "node27": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 90
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "42b45f8f-b991-41b5-bf29-a56b72f639f4"
        },
        "node28": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "dejittered-and-fir-eeg.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "E:/idatt2900_gr92/LSLData"
                },
                "preserve_original_metadata": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "ffcac90e-0fce-4850-b73c-28315a8605c7"
        },
        "node29": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 90
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "9af45682-556a-4e42-9985-3b5bb36c6eef"
        },
        "node3": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "apply_time_selection_to_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": [
                        "left_blink",
                        "left_openness",
                        "right_blink",
                        "right_openness",
                        "both_blink"
                    ]
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "names"
                }
            },
            "uuid": "478b0faf-7c39-4d23-94bd-7f7e5643e14b"
        },
        "node30": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "raw-eeg.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "E:/idatt2900_gr92/LSLData"
                },
                "preserve_original_metadata": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "cfd7ee67-34e0-457e-abc5-6c0fe2000674"
        },
        "node31": {
            "class": "MergeStreams",
            "module": "neuropype.nodes.formatting.MergeStreams",
            "params": {
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "replace_if_exists": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "sorting": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "input"
                }
            },
            "uuid": "2709fda6-da36-4012-87b7-b5cf928805a2"
        },
        "node32": {
            "class": "FuseStreams",
            "module": "neuropype.nodes.formatting.FuseStreams",
            "params": {
                "buffer_delay": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 2
                },
                "desired_headroom": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "min_headroom": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 2
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "srate": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 80
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "eeg"
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                }
            },
            "uuid": "84683d45-d99d-4f47-9088-a0ed17bf9eae"
        },
        "node33": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "dejittered-fir-eeg-and-dejittered-eyetracking.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "E:/idatt2900_gr92/LSLData"
                },
                "preserve_original_metadata": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "c7b18e4e-b007-43f8-bd8c-4268f3169842"
        },
        "node34": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "gaze-and-blinking.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "E:/idatt2900_gr92/LSLData"
                },
                "preserve_original_metadata": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "d41e2c91-fa48-4ce1-81fe-2bc33f607960"
        },
        "node35": {
            "class": "MergeStreams",
            "module": "neuropype.nodes.formatting.MergeStreams",
            "params": {
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "replace_if_exists": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "sorting": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "input"
                }
            },
            "uuid": "5705c43f-d396-46d7-b653-4470a68fbe2d"
        },
        "node36": {
            "class": "FuseStreams",
            "module": "neuropype.nodes.formatting.FuseStreams",
            "params": {
                "buffer_delay": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 2
                },
                "desired_headroom": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "min_headroom": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 2
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "srate": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 80
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "eeg"
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                }
            },
            "uuid": "e3be9f7a-3564-4711-b83a-e0e0b87c59f5"
        },
        "node37": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "dejittered-timestamp-shifted-106ms-eeg-and-dejittered-eyetracking.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "E:/idatt2900_gr92/LSLData"
                },
                "preserve_original_metadata": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "8af05c78-2a4a-44dc-874f-e0d06ee1fda2"
        },
        "node38": {
            "class": "ShiftTimestamps",
            "module": "neuropype.nodes.utilities.ShiftTimestamps",
            "params": {
                "beginning_from_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "compensate_filter_lag": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "include_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_fields": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "offset": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": -0.04
                },
                "offset_triggers_state_reset": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "timestamp_pairs": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "use_time_axis": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "3591181e-959a-4fe1-8f06-843d7fb281c4"
        },
        "node39": {
            "class": "MergeStreams",
            "module": "neuropype.nodes.formatting.MergeStreams",
            "params": {
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "replace_if_exists": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "sorting": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "input"
                }
            },
            "uuid": "4b30a56a-5a06-4645-92d6-d3d6c4631c1d"
        },
        "node4": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "Fp1",
                        "Fz",
                        "F3",
                        "F7",
                        "F9",
                        "FC5",
                        "FC1",
                        "C3",
                        "T7",
                        "CP5",
                        "CP1",
                        "Pz",
                        "P3",
                        "P7",
                        "P9",
                        "O1",
                        "Oz",
                        "O2",
                        "P10",
                        "P8",
                        "P4",
                        "CP2",
                        "CP6",
                        "T8",
                        "C4",
                        "Cz",
                        "FC2",
                        "FC6",
                        "F10",
                        "F8",
                        "F4",
                        "Fp2",
                        "ACC_X",
                        "ACC_Y",
                        "ACC_Z"
                    ]
                },
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "exclude_desc_fields": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "localhost_only": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_query": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "omit_desc": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "prealloc_buffer": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_clocksync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_dejitter": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_monotonize": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_threadsafe": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='LiveAmpSN-056309-0553'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "fbf7cab1-923c-4853-b2c3-8449dd016331"
        },
        "node40": {
            "class": "FuseStreams",
            "module": "neuropype.nodes.formatting.FuseStreams",
            "params": {
                "buffer_delay": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 2
                },
                "desired_headroom": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "min_headroom": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 2
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "srate": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 80
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "eeg"
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                }
            },
            "uuid": "2cc5c917-ea12-4d6e-8706-9e47aa7ff6d6"
        },
        "node41": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "dejittered-fir-timestamp-shifted-40ms-eeg-and-dejittered-eyetracking.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "E:/idatt2900_gr92/LSLData"
                },
                "preserve_original_metadata": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "505782a4-b0ee-4cd9-821f-fb1655095c6e"
        },
        "node42": {
            "class": "IIRFilter",
            "module": "neuropype.nodes.signal_processing.IIRFilter",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "design": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "butter"
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        1,
                        28
                    ]
                },
                "ignore_nans": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "offline_filtfilt": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "order": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 4
                },
                "pass_loss": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 3.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "66adcba7-2b2e-456d-9ef0-1c71de2259da"
        },
        "node43": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "dejittered-iir-eeg-and-dejittered-eyetracking.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "E:/idatt2900_gr92/LSLData"
                },
                "preserve_original_metadata": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "f2e41597-3424-43d3-8a2d-4f8d75511bfe"
        },
        "node44": {
            "class": "MergeStreams",
            "module": "neuropype.nodes.formatting.MergeStreams",
            "params": {
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "replace_if_exists": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "sorting": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "input"
                }
            },
            "uuid": "c1e4e933-fc09-4014-9f18-f7687145e2e1"
        },
        "node45": {
            "class": "FuseStreams",
            "module": "neuropype.nodes.formatting.FuseStreams",
            "params": {
                "buffer_delay": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 2
                },
                "desired_headroom": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "min_headroom": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 2
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "srate": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 80
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "eeg"
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                }
            },
            "uuid": "6edf1d33-6101-421e-a3b2-3dc530cb7e58"
        },
        "node46": {
            "class": "ConstantInt",
            "module": "neuropype.nodes.programming.ConstantInt",
            "params": {
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "value": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 80
                }
            },
            "uuid": "07008794-0d04-49d5-9445-e263ec1e7aea"
        },
        "node47": {
            "class": "ConstantString",
            "module": "neuropype.nodes.programming.ConstantString",
            "params": {
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "value": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "E:/idatt2900_gr92/LSLData"
                }
            },
            "uuid": "2a82deb2-e576-45d0-b6d4-2149b247aa19"
        },
        "node5": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_line_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "font_size": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 10.0
                },
                "initial_dims": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        720,
                        950,
                        700,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "max_channels": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 32
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "no_concatenate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5.0
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Time series EEG After Removal view"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "16841007-9b61-4851-a6a8-b0db09ccdd18"
        },
        "node6": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 90
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "900a5cab-ea32-4cbc-9b91-ff6b299ac459"
        },
        "node7": {
            "class": "FIRFilter",
            "module": "neuropype.nodes.signal_processing.FIRFilter",
            "params": {
                "antisymmetric": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "convolution_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "standard"
                },
                "cut_preringing": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "frequencies": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        0.25,
                        0.5,
                        45,
                        50
                    ]
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "minimum_phase": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "order": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "4c280301-0808-4812-9b17-042c123a565f"
        },
        "node8": {
            "class": "RemoveUnlocalizedChannels",
            "module": "neuropype.nodes.source_localization.RemoveUnlocalizedChannels",
            "params": {
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "protect_channels": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "54ad9cb7-2874-40f9-a832-5c6d13676e0c"
        },
        "node9": {
            "class": "BadChannelRemoval",
            "module": "neuropype.nodes.neural.BadChannelRemoval",
            "params": {
                "calib_seconds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 20
                },
                "coords_override": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "corr_threshold": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.8
                },
                "ignore_chanlocs": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "ignored_quantile": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.1
                },
                "init_on": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "keep_unlocalized_channels": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "linenoise_aware": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_bad_channels": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.15
                },
                "max_broken_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.4
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "min_corr": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "noise_threshold": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 4
                },
                "num_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 200
                },
                "protect_channels": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "rereferenced": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "subset_size": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.15
                },
                "use_clean_window": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "window_len": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "window_len_cleanwindow": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "window_overlap": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.66
                },
                "zscore_thresholds": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        -3.5,
                        5
                    ]
                }
            },
            "uuid": "31ffaa61-9eda-45af-bbcd-b288c8f49864"
        }
    },
    "version": 1.1
}</patch>
</scheme>
