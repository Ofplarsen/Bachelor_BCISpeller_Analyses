<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="EEGAndEyeTracker" version="2.0">
	<nodes>
		<node id="0" name="LSL Input" position="(1500, 800)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="ObjectPositionStream" uuid="886993b3-e015-4cee-be3f-036a6b4290a9" version="1.5.1" />
		<node id="1" name="LSL Input" position="(0, 200)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="EyeTrackerStream" uuid="1beb457e-99dd-48ac-8370-32a544c63ef7" version="1.5.1" />
		<node id="2" name="Select Range" position="(400, 300)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Blinking Data" uuid="34e7b9bb-28fc-4b28-a040-851390f1360a" version="1.1.0" />
		<node id="3" name="LSL Input" position="(0, 1300)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="EEG" uuid="23a0f320-33ae-4ffe-92cd-fb350ad17042" version="1.5.1" />
		<node id="4" name="Dejitter Timestamps" position="(200, 1300)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="573dacb6-b1c8-4fca-a4c7-a861cf5d2678" version="1.0.0" />
		<node id="5" name="Merge Streams" position="(500, 600)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams" uuid="153cd31d-628e-47e3-8561-0b1cbb896d89" version="1.0.0" />
		<node id="6" name="Fuse Streams" position="(700, 700)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams" uuid="c01f5f3c-1f04-44b3-80d4-70d1114f3233" version="0.9.6" />
		<node id="7" name="Record to XDF" position="(100, 300)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF" uuid="1947116c-f8a3-4f3c-a4f2-31957f7c0537" version="1.4.0" />
		<node id="8" name="Record to XDF" position="(800, 700)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (3)" uuid="a5af9fa4-9315-4098-a74e-9b41add6be63" version="1.4.0" />
		<node id="9" name="Record to XDF" position="(100, 1500)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (1)" uuid="e0c01721-0024-4226-844b-564ff9843e25" version="1.4.0" />
		<node id="10" name="Record to XDF" position="(1700, 900)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (2)" uuid="51392aec-1652-4ebe-b384-16a77b98a477" version="1.4.0" />
		<node id="11" name="Time Series Plot" position="(600, 200)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot (2)" uuid="f0f5f56d-3b79-4baf-a2be-0ca5d286fe5a" version="1.1.0" />
		<node id="12" name="Add Event Marker" position="(900, 300)" project_name="NeuroPype" qualified_name="widgets.markers.owaddeventmarker.OWAddEventMarker" title="Add Event Marker" uuid="46ce7de0-3a72-47c7-b5a1-b9e2b0266205" version="1.1.0" />
		<node id="13" name="Marker Stream Window" position="(1100, 300)" project_name="NeuroPype" qualified_name="widgets.visualization.owmarkerstreamwindow.OWMarkerStreamWindow" title="Marker Stream Window" uuid="9f841e53-5560-4703-976d-991b3abb3054" version="1.1.1" />
		<node id="14" name="Break Structure" position="(1200, 300)" project_name="NeuroPype" qualified_name="widgets.programming.owbreakstructure.OWBreakStructure" title="Break Structure" uuid="d1fd5f8c-63f6-4e88-8afd-1a5c725b0dbf" version="1.0.0" />
		<node id="15" name="Shift Timestamps" position="(334.0, 1228.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owshifttimestamps.OWShiftTimestamps" title="Shift Timestamps" uuid="5746b58a-399f-495a-b074-d0060939248b" version="1.2.1" />
		<node id="16" name="Inspect Packet" position="(300, 100)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectpacket.OWInspectPacket" title="Inspect Packet" uuid="94b88594-9dee-4b00-9a24-154b768f5c35" version="3.0.1" />
		<node id="17" name="Dejitter Timestamps" position="(100, 200)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps (2)" uuid="d75d5a04-133e-471a-aa47-219d253698c4" version="1.0.0" />
		<node id="18" name="Dejitter Timestamps" position="(1600, 800)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps (1)" uuid="b6aa18da-01b7-42d2-8b6a-8e027811d5a6" version="1.0.0" />
		<node id="19" name="Record to XDF" position="(0, 1500)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (5)" uuid="ce751895-4521-4096-97ee-40985a8e3dc1" version="1.4.0" />
		<node id="20" name="Record to XDF" position="(0, 300)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (7)" uuid="0f0a4146-943d-4c8a-bd65-b53886515dc6" version="1.4.0" />
		<node id="21" name="Merge Streams" position="(600, 900)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams (2)" uuid="c21ecbc4-97f5-4515-ac94-718feeee98ac" version="1.0.0" />
		<node id="22" name="Fuse Streams" position="(700, 900)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams (2)" uuid="b1335326-a3cd-44d4-b796-7a928a60da83" version="0.9.6" />
		<node id="23" name="Record to XDF" position="(800, 900)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (8)" uuid="d0730f37-fbb1-44c6-b61b-0e32aa4acdb5" version="1.4.0" />
		<node id="24" name="IIR Filter" position="(345.0, 1337.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="IIR Filter" uuid="1421bf9d-8441-4ed3-aa4a-100fdac90420" version="1.1.0" />
		<node id="25" name="Record to XDF" position="(880.0, 1312.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (9)" uuid="ed48b790-0d7f-4e15-b93f-dd6fcec2faf3" version="1.4.0" />
		<node id="26" name="Merge Streams" position="(634.0, 1307.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams (3)" uuid="572c6f4f-07c8-4d3b-9203-9ffa379a3740" version="1.0.0" />
		<node id="27" name="Fuse Streams" position="(749.0, 1309.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams (3)" uuid="549af808-3ef8-4c54-8e61-dced199d1eca" version="0.9.6" />
		<node id="28" name="Constant String" position="(100, 700)" project_name="NeuroPype" qualified_name="widgets.programming.owconstantstring.OWConstantString" title="Constant String" uuid="9c554161-6a56-428e-a717-ee04700c4a66" version="1.0.0" />
		<node id="29" name="Constant Integer" position="(0, 900)" project_name="NeuroPype" qualified_name="widgets.programming.owconstantint.OWConstantInt" title="Constant FPS" uuid="cd244cfd-4a23-4d8f-bd6a-c68ddace1dc2" version="1.0.0" />
		<node id="30" name="IIR Filter" position="(366.0, 1577.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="IIR Filter (1)" uuid="f609a2aa-35e8-4a33-a201-6ca4c9fe5460" version="1.1.0" />
		<node id="31" name="Merge Streams" position="(651.0, 1575.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams (4)" uuid="21713dd6-bd0f-4472-b743-903e87fffb67" version="1.0.0" />
		<node id="32" name="Fuse Streams" position="(767.0, 1577.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams (4)" uuid="27744b40-1ce0-4266-beac-0d1e40fc2d65" version="0.9.6" />
		<node id="33" name="Record to XDF" position="(902.0, 1582.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (6)" uuid="a0c781c6-2ba6-4fbf-9f2f-4d62e4abce2b" version="1.4.0" />
		<node id="34" name="IIR Filter" position="(353.0, 1441.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="IIR Filter (2)" uuid="011a6fae-08d1-4662-97a3-3ab51f77ee4a" version="1.1.0" />
		<node id="35" name="Merge Streams" position="(633.0, 1444.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams (1)" uuid="6c7c9a74-3484-40e2-a15b-acff44bbb4ef" version="1.0.0" />
		<node id="36" name="Fuse Streams" position="(757.0, 1440.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams (1)" uuid="5d2b8892-5e36-40ad-bf6f-11ee18a19d6d" version="0.9.6" />
		<node id="37" name="Record to XDF" position="(894.0, 1445.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (4)" uuid="64d77bf7-a24e-421f-a567-9211df0f0f67" version="1.4.0" />
		<node id="38" name="Merge Streams" position="(644.0, 1701.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams (4)" uuid="bb0d8df2-b91a-4df1-b68e-492e17373025" version="1.0.0" />
		<node id="39" name="IIR Filter" position="(360.0, 1703.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="IIR Filter (1)" uuid="d42a8fbe-489e-4dd5-8663-05d60176a628" version="1.1.0" />
		<node id="40" name="Fuse Streams" position="(760.0, 1703.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams (4)" uuid="af385ce8-10ca-493e-8790-d0a69b4a708d" version="0.9.6" />
		<node id="41" name="Record to XDF" position="(895.0, 1707.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (6)" uuid="eefb1dae-e803-4b7f-b2f6-c97a3952f932" version="1.4.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="6" source_channel="Outdata" source_node_id="5" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="2" />
		<link enabled="false" id="4" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="6" sink_channel="Data2" sink_node_id="5" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="17" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="16" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="10" sink_channel="Data1" sink_node_id="5" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="18" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="14" sink_channel="Data" sink_node_id="19" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="15" sink_channel="Data" sink_node_id="20" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="16" sink_channel="Data" sink_node_id="15" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="17" sink_channel="Data2" sink_node_id="21" source_channel="Data" source_node_id="15" />
		<link enabled="true" id="18" sink_channel="Data1" sink_node_id="21" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="19" sink_channel="Data" sink_node_id="22" source_channel="Outdata" source_node_id="21" />
		<link enabled="true" id="20" sink_channel="Data" sink_node_id="23" source_channel="Data" source_node_id="22" />
		<link enabled="false" id="21" sink_channel="Data" sink_node_id="24" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="22" sink_channel="Data" sink_node_id="25" source_channel="Data" source_node_id="27" />
		<link enabled="true" id="23" sink_channel="Data" sink_node_id="27" source_channel="Outdata" source_node_id="26" />
		<link enabled="true" id="24" sink_channel="Data2" sink_node_id="26" source_channel="Data" source_node_id="24" />
		<link enabled="false" id="25" sink_channel="Data1" sink_node_id="26" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="26" sink_channel="Output Root" sink_node_id="8" source_channel="Data" source_node_id="28" />
		<link enabled="true" id="27" sink_channel="Output Root" sink_node_id="23" source_channel="Data" source_node_id="28" />
		<link enabled="true" id="28" sink_channel="Output Root" sink_node_id="25" source_channel="Data" source_node_id="28" />
		<link enabled="true" id="29" sink_channel="Output Root" sink_node_id="7" source_channel="Data" source_node_id="28" />
		<link enabled="true" id="30" sink_channel="Output Root" sink_node_id="20" source_channel="Data" source_node_id="28" />
		<link enabled="true" id="31" sink_channel="Output Root" sink_node_id="9" source_channel="Data" source_node_id="28" />
		<link enabled="true" id="32" sink_channel="Output Root" sink_node_id="19" source_channel="Data" source_node_id="28" />
		<link enabled="true" id="33" sink_channel="Output Sampling Rate" sink_node_id="27" source_channel="Data" source_node_id="29" />
		<link enabled="true" id="34" sink_channel="Output Sampling Rate" sink_node_id="22" source_channel="Data" source_node_id="29" />
		<link enabled="true" id="35" sink_channel="Output Sampling Rate" sink_node_id="6" source_channel="Data" source_node_id="29" />
		<link enabled="false" id="36" sink_channel="Data" sink_node_id="30" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="37" sink_channel="Data2" sink_node_id="31" source_channel="Data" source_node_id="30" />
		<link enabled="false" id="38" sink_channel="Data1" sink_node_id="31" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="39" sink_channel="Data" sink_node_id="32" source_channel="Outdata" source_node_id="31" />
		<link enabled="true" id="40" sink_channel="Data" sink_node_id="33" source_channel="Data" source_node_id="32" />
		<link enabled="true" id="41" sink_channel="Output Root" sink_node_id="33" source_channel="Data" source_node_id="28" />
		<link enabled="true" id="42" sink_channel="Output Sampling Rate" sink_node_id="32" source_channel="Data" source_node_id="29" />
		<link enabled="false" id="43" sink_channel="Data" sink_node_id="34" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="44" sink_channel="Data2" sink_node_id="35" source_channel="Data" source_node_id="34" />
		<link enabled="false" id="45" sink_channel="Data1" sink_node_id="35" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="46" sink_channel="Data" sink_node_id="36" source_channel="Outdata" source_node_id="35" />
		<link enabled="true" id="47" sink_channel="Output Sampling Rate" sink_node_id="36" source_channel="Data" source_node_id="29" />
		<link enabled="true" id="48" sink_channel="Data" sink_node_id="37" source_channel="Data" source_node_id="36" />
		<link enabled="true" id="49" sink_channel="Output Root" sink_node_id="37" source_channel="Data" source_node_id="28" />
		<link enabled="true" id="50" sink_channel="Data" sink_node_id="40" source_channel="Outdata" source_node_id="38" />
		<link enabled="true" id="51" sink_channel="Data" sink_node_id="41" source_channel="Data" source_node_id="40" />
		<link enabled="true" id="52" sink_channel="Data" sink_node_id="39" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="53" sink_channel="Output Sampling Rate" sink_node_id="40" source_channel="Data" source_node_id="29" />
		<link enabled="true" id="54" sink_channel="Output Root" sink_node_id="41" source_channel="Data" source_node_id="28" />
		<link enabled="true" id="55" sink_channel="Data1" sink_node_id="38" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="56" sink_channel="Data2" sink_node_id="38" source_channel="Data" source_node_id="39" />
	</links>
	<annotations>
		<text font-family="Helvetica" font-size="16" id="0" rect="(-116.0, 1217.0, 244.0, 62.0)">LSL stream for EEG and cleaning up data.</text>
		<text font-family="Helvetica" font-size="16" id="1" rect="(1494.0, 677.0, 207.0, 88.0)">LSL stream for when objects are looked at and their position.</text>
		<text font-family="Helvetica" font-size="16" id="2" rect="(-34.0, 61.0, 198.0, 50.0)">LSL stream for eye tracking and blinking.</text>
		<text font-family="Helvetica" font-size="16" id="3" rect="(903.0, 632.0, 368.0, 31.0)">Merging dejittered eye tracking and dejittered EEG</text>
		<text font-family="Helvetica" font-size="16" id="4" rect="(896.0, 903.0, 319.0, 69.0)">Mergiing dejittered eye tracking and dejittered + timestamp shifted EEG
</text>
		<text font-family="Helvetica" font-size="16" id="5" rect="(936.0, 1290.0, 348.0, 69.0)">Mergiing dejittered eye tracking and dejittered + IIR butter 4th order, [1,24] EEG</text>
		<text font-family="Helvetica" font-size="16" id="6" rect="(-68.0, 813.0, 139.0, 69.0)">Sampling rate for fused streams</text>
		<text font-family="Helvetica" font-size="16" id="7" rect="(13.0, 643.0, 252.0, 83.0)">String containing root for recordings</text>
		<text font-family="Helvetica" font-size="16" id="8" rect="(956.0, 1562.0, 349.0, 69.0)">Merging dejittered eye tracking and dejittered + IIR 3rd order, [1, 24], EEG</text>
		<text font-family="Helvetica" font-size="16" id="9" rect="(946.0, 1424.0, 348.0, 78.0)">Merging dejittered eye tracking and dejittered + IIR 4th order, [0.75,5] EEG</text>
		<text font-family="Helvetica" font-size="16" id="10" rect="(948.0, 1690.0, 340.0, 59.0)">Merging dejittered eye tracking and dejittered + IIR 3rd order, [0.75, 5], EEG</text>
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
		<properties format="literal" node_id="4">{'force_monotonic': True, 'forget_halftime': 90, 'max_updaterate': 500, 'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'warmup_samples': -1}</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBEAAAByZXBsYWNlX2lmX2V4aXN0c3EDiVgTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDUuUXRDb3Jl
cQZYCgAAAFFCeXRlQXJyYXlxB0NCAdnQywADAAAAAAbCAAADjAAACCsAAASFAAAGwwAAA7kAAAgq
AAAEhAAAAAAAAAAADwAAAAbDAAADuQAACCoAAASEcQiFcQmHcQpScQtYDgAAAHNldF9icmVha3Bv
aW50cQyJWAcAAABzb3J0aW5ncQ1YBQAAAGlucHV0cQ51Lg==
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAwAAABidWZmZXJfZGVsYXlxAUsCWBAAAABkZXNpcmVkX2hlYWRyb29tcQJLBVgIAAAA
bWV0YWRhdGFxA31xBFgMAAAAbWluX2hlYWRyb29tcQVLAlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJy
YXlxCUNCAdnQywADAAAAAAavAAADSAAACD4AAATJAAAGsAAAA3UAAAg9AAAEyAAAAAAAAAAADwAA
AAawAAADdQAACD0AAATIcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAUAAABzcmF0
ZXEPS1BYCwAAAHN0cmVhbV9uYW1lcRBYAwAAAGVlZ3ERWAkAAAB2ZXJib3NpdHlxEksBdS4=
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYIAAAAGRlaml0dGVyZWQtZ2F6ZS1hbmQtYmxpbmtpbmcueGRmcQ1YCAAAAG1ldGFkYXRh
cQ59cQ9YCwAAAG91dHB1dF9yb290cRBoBVgaAAAAcHJlc2VydmVfb3JpZ2luYWxfbWV0YWRhdGFx
EYlYCwAAAHJldHJpZXZhYmxlcRKJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRNjc2lwCl91bnBp
Y2tsZV90eXBlCnEUWAwAAABQeVF0NS5RdENvcmVxFVgKAAAAUUJ5dGVBcnJheXEWQ0IB2dDLAAMA
AAAABsIAAALWAAAIKwAABTsAAAbDAAADAwAACCoAAAU6AAAAAAAAAAAPAAAABsMAAAMDAAAIKgAA
BTpxF4VxGIdxGVJxGlgNAAAAc2Vzc2lvbl9ub3Rlc3EbaAVYDgAAAHNldF9icmVha3BvaW50cRyJ
WAcAAAB2ZXJib3NlcR2JdS4=
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYLQAAAGRlaml0dGVyZWQtZWVnLWFuZC1kZWppdHRlcmVkLWV5ZXRyYWNraW5nLnhkZnEN
WAgAAABtZXRhZGF0YXEOfXEPWAsAAABvdXRwdXRfcm9vdHEQaAVYGgAAAHByZXNlcnZlX29yaWdp
bmFsX21ldGFkYXRhcRGJWAsAAAByZXRyaWV2YWJsZXESiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXETY3NpcApfdW5waWNrbGVfdHlwZQpxFFgMAAAAUHlRdDUuUXRDb3JlcRVYCgAAAFFCeXRlQXJy
YXlxFkNCAdnQywADAAAAAAaFAAAD5wAACPUAAAZMAAAGhgAABBQAAAj0AAAGSwAAAAAAAAAADwAA
AAaGAAAEFAAACPQAAAZLcReFcRiHcRlScRpYDQAAAHNlc3Npb25fbm90ZXNxG2gFWA4AAABzZXRf
YnJlYWtwb2ludHEciVgHAAAAdmVyYm9zZXEdiXUu
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYEgAAAGRlaml0dGVyZWQtZWVnLnhkZnENWAgAAABtZXRhZGF0YXEOfXEPWAsAAABvdXRw
dXRfcm9vdHEQaAVYGgAAAHByZXNlcnZlX29yaWdpbmFsX21ldGFkYXRhcRGJWAsAAAByZXRyaWV2
YWJsZXESiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXETY3NpcApfdW5waWNrbGVfdHlwZQpxFFgM
AAAAUHlRdDUuUXRDb3JlcRVYCgAAAFFCeXRlQXJyYXlxFkNCAdnQywADAAAAAAbCAAAC1gAACCsA
AAU7AAAGwwAAAwMAAAgqAAAFOgAAAAAAAAAADwAAAAbDAAADAwAACCoAAAU6cReFcRiHcRlScRpY
DQAAAHNlc3Npb25fbm90ZXNxG2gFWA4AAABzZXRfYnJlYWtwb2ludHEciVgHAAAAdmVyYm9zZXEd
iXUu
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYCwAAAG9iai1wb3MueGRmcQ1YCAAAAG1ldGFkYXRhcQ59cQ9YCwAAAG91dHB1dF9yb290
cRBYGQAAAEU6L2lkYXR0MjkwMF9ncjkyL0xTTERhdGFxEVgaAAAAcHJlc2VydmVfb3JpZ2luYWxf
bWV0YWRhdGFxEolYCwAAAHJldHJpZXZhYmxlcROJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRRj
c2lwCl91bnBpY2tsZV90eXBlCnEVWAwAAABQeVF0NS5RdENvcmVxFlgKAAAAUUJ5dGVBcnJheXEX
Q0IB2dDLAAMAAAAABsIAAALWAAAIKwAABTsAAAbDAAADAwAACCoAAAU6AAAAAAAAAAAPAAAABsMA
AAMDAAAIKgAABTpxGIVxGYdxGlJxG1gNAAAAc2Vzc2lvbl9ub3Rlc3EcaAVYDgAAAHNldF9icmVh
a3BvaW50cR2JWAcAAAB2ZXJib3NlcR6JdS4=
</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGIWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
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
		<properties format="pickle" node_id="12">gAN9cQAoWA4AAABldmVudF90b19tYXRjaHEBWAAAAABxAlgWAAAAbWF0Y2hfZmlyc3RfZXZlbnRf
b25seXEDiVgIAAAAbWV0YWRhdGFxBH1xBVgQAAAAbmV3X2V2ZW50X21hcmtlcnEGaAJYEwAAAHNh
dmVkV2lkZ2V0R2VvbWV0cnlxB2NzaXAKX3VucGlja2xlX3R5cGUKcQhYDAAAAFB5UXQ1LlF0Q29y
ZXEJWAoAAABRQnl0ZUFycmF5cQpDQgHZ0MsAAwAAAAAJEQAAAckAAAp/AAADgAAACRIAAAH2AAAK
fgAAA38AAAAAAAAAAA8AAAAJEgAAAfYAAAp+AAADf3ELhXEMh3ENUnEOWA4AAABzZXRfYnJlYWtw
b2ludHEPiVgGAAAAc3RyZWFtcRBoAlgOAAAAdHJpYWxfY3JpdGVyaWFxEV1xElgMAAAAbGVmdF9i
bGluaz0xcRNhWAkAAAB0cmlhbF9lbmRxFGgCWAsAAAB0cmlhbF9zdGFydHEVaAJYBwAAAHZlcmJv
c2VxFol1Lg==
</properties>
		<properties format="literal" node_id="13">{'always_on_top': False, 'initial_dims': [50, 50, 500, 500], 'metadata': {}, 'override_srate': '(use default)', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'stream_name': 'Markers'}</properties>
		<properties format="literal" node_id="14">{'default0': '(use default)', 'default1': '(use default)', 'default10': '(use default)', 'default11': '(use default)', 'default12': '(use default)', 'default13': '(use default)', 'default14': '(use default)', 'default2': '(use default)', 'default3': '(use default)', 'default4': '(use default)', 'default5': '(use default)', 'default6': '(use default)', 'default7': '(use default)', 'default8': '(use default)', 'default9': '(use default)', 'defaults_type': 'str', 'metadata': {}, 'name0': '(use default)', 'name1': '(use default)', 'name10': '(use default)', 'name11': '(use default)', 'name12': '(use default)', 'name13': '(use default)', 'name14': '(use default)', 'name2': '(use default)', 'name3': '(use default)', 'name4': '(use default)', 'name5': '(use default)', 'name6': '(use default)', 'name7': '(use default)', 'name8': '(use default)', 'name9': '(use default)', 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWBMAAABiZWdpbm5pbmdfZnJvbV96ZXJvcQGJWBUAAABjb21wZW5zYXRlX2ZpbHRlcl9s
YWdxAolYDwAAAGluY2x1ZGVfbWFya2Vyc3EDiVgNAAAAbWFya2VyX2ZpZWxkc3EEWA0AAAAodXNl
IGRlZmF1bHQpcQVYCAAAAG1ldGFkYXRhcQZ9cQdYBgAAAG9mZnNldHEIR7+V7IDHOryUWBsAAABv
ZmZzZXRfdHJpZ2dlcnNfc3RhdGVfcmVzZXRxCYhYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxCmNz
aXAKX3VucGlja2xlX3R5cGUKcQtYDAAAAFB5UXQ1LlF0Q29yZXEMWAoAAABRQnl0ZUFycmF5cQ1D
QgHZ0MsAAwAAAAAGbwAAAzEAAAfYAAAE2QAABnAAAANeAAAH1wAABNgAAAAAAAAAAA8AAAAGcAAA
A14AAAfXAAAE2HEOhXEPh3EQUnERWA4AAABzZXRfYnJlYWtwb2ludHESiVgPAAAAdGltZXN0YW1w
X3BhaXJzcRNYDQAAACh1c2UgZGVmYXVsdClxFFgNAAAAdXNlX3RpbWVfYXhpc3EViHUu
</properties>
		<properties format="literal" node_id="16">{'always_on_top': True, 'col_axis': 'time', 'decimals': 6, 'every_n_ticks': 1, 'fewer_buttons': False, 'font_size': 10, 'initial_position': [20, 50, 500, 400], 'metadata': {}, 'row_axis': 'space', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'show_axes_table': True, 'show_data_table': True, 'show_markers_table': False, 'show_max_columns': 20, 'show_max_values': 50, 'show_streams_table': False, 'stream_name': '(use default)', 'verbose': True, 'window_title': 'Inspect Data Packet'}</properties>
		<properties format="pickle" node_id="17">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECS1pYDgAA
AG1heF91cGRhdGVyYXRlcQNN9AFYCAAAAG1ldGFkYXRhcQR9cQVYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxBmNzaXAKX3VucGlja2xlX3R5cGUKcQdYDAAAAFB5UXQ1LlF0Q29yZXEIWAoAAABRQnl0
ZUFycmF5cQlDQgHZ0MsAAwAAAAAGqgAAA2sAAAhEAAAEpwAABqsAAAOYAAAIQwAABKYAAAAAAAAA
AA8AAAAGqwAAA5gAAAhDAAAEpnEKhXELh3EMUnENWA4AAABzZXRfYnJlYWtwb2ludHEOiVgOAAAA
d2FybXVwX3NhbXBsZXNxD0r/////dS4=
</properties>
		<properties format="literal" node_id="18">{'force_monotonic': True, 'forget_halftime': 90, 'max_updaterate': 500, 'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'warmup_samples': -1}</properties>
		<properties format="pickle" node_id="19">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYCwAAAHJhdy1lZWcueGRmcQ1YCAAAAG1ldGFkYXRhcQ59cQ9YCwAAAG91dHB1dF9yb290
cRBoBVgaAAAAcHJlc2VydmVfb3JpZ2luYWxfbWV0YWRhdGFxEYlYCwAAAHJldHJpZXZhYmxlcRKJ
WBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRNjc2lwCl91bnBpY2tsZV90eXBlCnEUWAwAAABQeVF0
NS5RdENvcmVxFVgKAAAAUUJ5dGVBcnJheXEWQ0IB2dDLAAMAAAAABsMAAAMDAAAIKgAABToAAAbD
AAADAwAACCoAAAU6AAAAAAAAAAAPAAAABsMAAAMDAAAIKgAABTpxF4VxGIdxGVJxGlgNAAAAc2Vz
c2lvbl9ub3Rlc3EbaAVYDgAAAHNldF9icmVha3BvaW50cRyJWAcAAAB2ZXJib3NlcR2JdS4=
</properties>
		<properties format="pickle" node_id="20">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYFQAAAGdhemUtYW5kLWJsaW5raW5nLnhkZnENWAgAAABtZXRhZGF0YXEOfXEPWAsAAABv
dXRwdXRfcm9vdHEQaAVYGgAAAHByZXNlcnZlX29yaWdpbmFsX21ldGFkYXRhcRGJWAsAAAByZXRy
aWV2YWJsZXESiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXETY3NpcApfdW5waWNrbGVfdHlwZQpx
FFgMAAAAUHlRdDUuUXRDb3JlcRVYCgAAAFFCeXRlQXJyYXlxFkNCAdnQywADAAAAAAbCAAAC1gAA
CCsAAAU7AAAGwwAAAwMAAAgqAAAFOgAAAAAAAAAADwAAAAbDAAADAwAACCoAAAU6cReFcRiHcRlS
cRpYDQAAAHNlc3Npb25fbm90ZXNxG2gFWA4AAABzZXRfYnJlYWtwb2ludHEciVgHAAAAdmVyYm9z
ZXEdiXUu
</properties>
		<properties format="literal" node_id="21">{'metadata': {}, 'replace_if_exists': False, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'sorting': 'input'}</properties>
		<properties format="pickle" node_id="22">gAN9cQAoWAwAAABidWZmZXJfZGVsYXlxAUsCWBAAAABkZXNpcmVkX2hlYWRyb29tcQJLBVgIAAAA
bWV0YWRhdGFxA31xBFgMAAAAbWluX2hlYWRyb29tcQVLAlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJy
YXlxCUNCAdnQywADAAAAAAavAAADSAAACD4AAATJAAAGsAAAA3UAAAg9AAAEyAAAAAAAAAAADwAA
AAawAAADdQAACD0AAATIcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAUAAABzcmF0
ZXEPS3hYCwAAAHN0cmVhbV9uYW1lcRBYAwAAAGVlZ3ERWAkAAAB2ZXJib3NpdHlxEksBdS4=
</properties>
		<properties format="pickle" node_id="23">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYRQAAAGRlaml0dGVyZWQtdGltZXN0YW1wLXNoaWZ0ZWQtMTA2bXMtZWVnLWFuZC1kZWpp
dHRlcmVkLWV5ZXRyYWNraW5nLnhkZnENWAgAAABtZXRhZGF0YXEOfXEPWAsAAABvdXRwdXRfcm9v
dHEQaAVYGgAAAHByZXNlcnZlX29yaWdpbmFsX21ldGFkYXRhcRGJWAsAAAByZXRyaWV2YWJsZXES
iVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXETY3NpcApfdW5waWNrbGVfdHlwZQpxFFgMAAAAUHlR
dDUuUXRDb3JlcRVYCgAAAFFCeXRlQXJyYXlxFkNCAdnQywADAAAAAAbCAAAC1gAACSsAAAU7AAAG
wwAAAwMAAAkqAAAFOgAAAAAAAAAADwAAAAbDAAADAwAACSoAAAU6cReFcRiHcRlScRpYDQAAAHNl
c3Npb25fbm90ZXNxG2gFWA4AAABzZXRfYnJlYWtwb2ludHEciVgHAAAAdmVyYm9zZXEdiXUu
</properties>
		<properties format="pickle" node_id="24">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEsBSxhlWAsAAABpZ25vcmVfbmFuc3EHiVgIAAAAbWV0YWRhdGFx
CH1xCVgEAAAAbW9kZXEKWAgAAABiYW5kcGFzc3ELWBAAAABvZmZsaW5lX2ZpbHRmaWx0cQyJWAUA
AABvcmRlcnENSwRYCQAAAHBhc3NfbG9zc3EOR0AIAAAAAAAAWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cQ9jc2lwCl91bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0NS5RdENvcmVxEVgKAAAAUUJ5dGVB
cnJheXESQ0IB2dDLAAMAAAAABHEAAAM2AAAF/gAABQQAAARyAAADYwAABf0AAAUDAAAAAAAAAAAP
AAAABHIAAANjAAAF/QAABQNxE4VxFIdxFVJxFlgOAAAAc2V0X2JyZWFrcG9pbnRxF4lYCgAAAHN0
b3BfYXR0ZW5xGEdASQAAAAAAAHUu
</properties>
		<properties format="pickle" node_id="25">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYPgAAAGRlaml0dGVyZWQtaWlyLTRvcmRlci0xdG8yNC1lZWctYW5kLWRlaml0dGVyZWQt
ZXlldHJhY2tpbmcueGRmcQ1YCAAAAG1ldGFkYXRhcQ59cQ9YCwAAAG91dHB1dF9yb290cRBoBVga
AAAAcHJlc2VydmVfb3JpZ2luYWxfbWV0YWRhdGFxEYlYCwAAAHJldHJpZXZhYmxlcRKJWBMAAABz
YXZlZFdpZGdldEdlb21ldHJ5cRNjc2lwCl91bnBpY2tsZV90eXBlCnEUWAwAAABQeVF0NS5RdENv
cmVxFVgKAAAAUUJ5dGVBcnJheXEWQ0IB2dDLAAMAAAAABsIAAALWAAAJYAAABTsAAAbDAAADAwAA
CV8AAAU6AAAAAAAAAAAPAAAABsMAAAMDAAAJXwAABTpxF4VxGIdxGVJxGlgNAAAAc2Vzc2lvbl9u
b3Rlc3EbaAVYDgAAAHNldF9icmVha3BvaW50cRyJWAcAAAB2ZXJib3NlcR2JdS4=
</properties>
		<properties format="pickle" node_id="26">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBEAAAByZXBsYWNlX2lmX2V4aXN0c3EDiVgTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDUuUXRDb3Jl
cQZYCgAAAFFCeXRlQXJyYXlxB0NCAdnQywADAAAAAAbCAAADjAAACCsAAASFAAAGwwAAA7kAAAgq
AAAEhAAAAAAAAAAADwAAAAbDAAADuQAACCoAAASEcQiFcQmHcQpScQtYDgAAAHNldF9icmVha3Bv
aW50cQyJWAcAAABzb3J0aW5ncQ1YBQAAAGlucHV0cQ51Lg==
</properties>
		<properties format="pickle" node_id="27">gAN9cQAoWAwAAABidWZmZXJfZGVsYXlxAUsCWBAAAABkZXNpcmVkX2hlYWRyb29tcQJLBVgIAAAA
bWV0YWRhdGFxA31xBFgMAAAAbWluX2hlYWRyb29tcQVLAlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJy
YXlxCUNCAdnQywADAAAAAAawAAADdQAACD0AAATsAAAGsAAAA3UAAAg9AAAE7AAAAAAAAAAADwAA
AAawAAADdQAACD0AAATscQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAUAAABzcmF0
ZXEPS3hYCwAAAHN0cmVhbV9uYW1lcRBYAwAAAGVlZ3ERWAkAAAB2ZXJib3NpdHlxEksBdS4=
</properties>
		<properties format="pickle" node_id="28">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQNjc2lwCl91
bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NS5RdENvcmVxBVgKAAAAUUJ5dGVBcnJheXEGQ0IB2dDL
AAMAAAAABsIAAAOYAAAJlgAABHkAAAbDAAADxQAACZUAAAR4AAAAAAAAAAAPAAAABsMAAAPFAAAJ
lQAABHhxB4VxCIdxCVJxClgOAAAAc2V0X2JyZWFrcG9pbnRxC4lYBQAAAHZhbHVlcQxYPgAAAEM6
L1VzZXJzL3ZpemxhYl9zdHVkL2lkYXR0MjkwMF9ncjkyL25ldXJvcHlwZS1waXBlbGluZS9MU0xE
YXRhcQ11Lg==
</properties>
		<properties format="pickle" node_id="29">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQNjc2lwCl91
bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NS5RdENvcmVxBVgKAAAAUUJ5dGVBcnJheXEGQ0IB2dDL
AAMAAAAABsIAAAO2AAAIKwAABJcAAAbDAAAD4wAACCoAAASWAAAAAAAAAAAPAAAABsMAAAPjAAAI
KgAABJZxB4VxCIdxCVJxClgOAAAAc2V0X2JyZWFrcG9pbnRxC4lYBQAAAHZhbHVlcQxLeHUu
</properties>
		<properties format="pickle" node_id="30">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEsBSxhlWAsAAABpZ25vcmVfbmFuc3EHiVgIAAAAbWV0YWRhdGFx
CH1xCVgEAAAAbW9kZXEKWAgAAABiYW5kcGFzc3ELWBAAAABvZmZsaW5lX2ZpbHRmaWx0cQyJWAUA
AABvcmRlcnENSwNYCQAAAHBhc3NfbG9zc3EOR0AIAAAAAAAAWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cQ9jc2lwCl91bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0NS5RdENvcmVxEVgKAAAAUUJ5dGVB
cnJheXESQ0IB2dDLAAMAAAAACMgAAANoAAAKLwAABQgAAAjIAAADaAAACi8AAAUIAAAAAAAAAAAP
AAAACMgAAANoAAAKLwAABQhxE4VxFIdxFVJxFlgOAAAAc2V0X2JyZWFrcG9pbnRxF4lYCgAAAHN0
b3BfYXR0ZW5xGEdASQAAAAAAAHUu
</properties>
		<properties format="literal" node_id="31">{'metadata': {}, 'replace_if_exists': False, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'sorting': 'input'}</properties>
		<properties format="literal" node_id="32">{'buffer_delay': 2, 'desired_headroom': 5, 'metadata': {}, 'min_headroom': 2, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'srate': 125, 'stream_name': 'eeg', 'verbosity': 1}</properties>
		<properties format="pickle" node_id="33">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYPgAAAGRlaml0dGVyZWQtaWlyLTNvcmRlci0xdG8yNC1lZWctYW5kLWRlaml0dGVyZWQt
ZXlldHJhY2tpbmcueGRmcQ1YCAAAAG1ldGFkYXRhcQ59cQ9YCwAAAG91dHB1dF9yb290cRBoBVga
AAAAcHJlc2VydmVfb3JpZ2luYWxfbWV0YWRhdGFxEYlYCwAAAHJldHJpZXZhYmxlcRKJWBMAAABz
YXZlZFdpZGdldEdlb21ldHJ5cRNjc2lwCl91bnBpY2tsZV90eXBlCnEUWAwAAABQeVF0NS5RdENv
cmVxFVgKAAAAUUJ5dGVBcnJheXEWQ0IB2dDLAAMAAAAAA+0AAALZAAAGbAAABT4AAAPuAAADBgAA
BmsAAAU9AAAAAAAAAAAPAAAAA+4AAAMGAAAGawAABT1xF4VxGIdxGVJxGlgNAAAAc2Vzc2lvbl9u
b3Rlc3EbaAVYDgAAAHNldF9icmVha3BvaW50cRyJWAcAAAB2ZXJib3NlcR2JdS4=
</properties>
		<properties format="pickle" node_id="34">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEc/6AAAAAAAAEsFZVgLAAAAaWdub3JlX25hbnNxB4lYCAAAAG1l
dGFkYXRhcQh9cQlYBAAAAG1vZGVxClgIAAAAYmFuZHBhc3NxC1gQAAAAb2ZmbGluZV9maWx0Zmls
dHEMiVgFAAAAb3JkZXJxDUsEWAkAAABwYXNzX2xvc3NxDksDWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cQ9jc2lwCl91bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0NS5RdENvcmVxEVgKAAAAUUJ5dGVB
cnJheXESQ0IB2dDLAAMAAAAABnkAAAMzAAAIBgAABSUAAAZ6AAADYAAACAUAAAUkAAAAAAAAAAAP
AAAABnoAAANgAAAIBQAABSRxE4VxFIdxFVJxFlgOAAAAc2V0X2JyZWFrcG9pbnRxF4lYCgAAAHN0
b3BfYXR0ZW5xGEdASQAAAAAAAHUu
</properties>
		<properties format="literal" node_id="35">{'metadata': {}, 'replace_if_exists': False, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'sorting': 'input'}</properties>
		<properties format="literal" node_id="36">{'buffer_delay': 2, 'desired_headroom': 5, 'metadata': {}, 'min_headroom': 2, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'srate': 125, 'stream_name': 'eeg', 'verbosity': 1}</properties>
		<properties format="pickle" node_id="37">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYQAAAAGRlaml0dGVyZWQtaWlyLTRvcmRlci0wLjc1dG81LWVlZy1hbmQtZGVqaXR0ZXJl
ZC1leWV0cmFja2luZy54ZGZxDVgIAAAAbWV0YWRhdGFxDn1xD1gLAAAAb3V0cHV0X3Jvb3RxEGgF
WBoAAABwcmVzZXJ2ZV9vcmlnaW5hbF9tZXRhZGF0YXERiVgLAAAAcmV0cmlldmFibGVxEolYEwAA
AHNhdmVkV2lkZ2V0R2VvbWV0cnlxE2NzaXAKX3VucGlja2xlX3R5cGUKcRRYDAAAAFB5UXQ1LlF0
Q29yZXEVWAoAAABRQnl0ZUFycmF5cRZDQgHZ0MsAAwAAAAAGwgAAAtYAAAkaAAAFOwAABsMAAAMD
AAAJGQAABToAAAAAAAAAAA8AAAAGwwAAAwMAAAkZAAAFOnEXhXEYh3EZUnEaWA0AAABzZXNzaW9u
X25vdGVzcRtoBVgOAAAAc2V0X2JyZWFrcG9pbnRxHIlYBwAAAHZlcmJvc2VxHYl1Lg==
</properties>
		<properties format="pickle" node_id="38">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWBEAAAByZXBsYWNlX2lmX2V4aXN0c3EDiVgTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDUuUXRDb3Jl
cQZYCgAAAFFCeXRlQXJyYXlxB0NCAdnQywADAAAAAAbCAAADjAAACCsAAASFAAAGwwAAA7kAAAgq
AAAEhAAAAAAAAAAADwAAAAbDAAADuQAACCoAAASEcQiFcQmHcQpScQtYDgAAAHNldF9icmVha3Bv
aW50cQyJWAcAAABzb3J0aW5ncQ1YBQAAAGlucHV0cQ51Lg==
</properties>
		<properties format="pickle" node_id="39">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEc/6AAAAAAAAEsFZVgLAAAAaWdub3JlX25hbnNxB4lYCAAAAG1l
dGFkYXRhcQh9cQlYBAAAAG1vZGVxClgIAAAAYmFuZHBhc3NxC1gQAAAAb2ZmbGluZV9maWx0Zmls
dHEMiVgFAAAAb3JkZXJxDUsDWAkAAABwYXNzX2xvc3NxDkdACAAAAAAAAFgTAAAAc2F2ZWRXaWRn
ZXRHZW9tZXRyeXEPY3NpcApfdW5waWNrbGVfdHlwZQpxEFgMAAAAUHlRdDUuUXRDb3JlcRFYCgAA
AFFCeXRlQXJyYXlxEkNCAdnQywADAAAAAAawAAADIgAACD0AAATwAAAGsQAAA08AAAg8AAAE7wAA
AAAAAAAADwAAAAaxAAADTwAACDwAAATvcROFcRSHcRVScRZYDgAAAHNldF9icmVha3BvaW50cReJ
WAoAAABzdG9wX2F0dGVucRhHQEkAAAAAAAB1Lg==
</properties>
		<properties format="literal" node_id="40">{'buffer_delay': 2, 'desired_headroom': 5, 'metadata': {}, 'min_headroom': 2, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'srate': 125, 'stream_name': 'eeg', 'verbosity': 1}</properties>
		<properties format="pickle" node_id="41">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYQAAAAGRlaml0dGVyZWQtaWlyLTNvcmRlci0wLjc1dG81LWVlZy1hbmQtZGVqaXR0ZXJl
ZC1leWV0cmFja2luZy54ZGZxDVgIAAAAbWV0YWRhdGFxDn1xD1gLAAAAb3V0cHV0X3Jvb3RxEGgF
WBoAAABwcmVzZXJ2ZV9vcmlnaW5hbF9tZXRhZGF0YXERiVgLAAAAcmV0cmlldmFibGVxEolYEwAA
AHNhdmVkV2lkZ2V0R2VvbWV0cnlxE2NzaXAKX3VucGlja2xlX3R5cGUKcRRYDAAAAFB5UXQ1LlF0
Q29yZXEVWAoAAABRQnl0ZUFycmF5cRZDQgHZ0MsAAwAAAAAGwgAAAtYAAAmPAAAFOwAABsMAAAMD
AAAJjgAABToAAAAAAAAAAA8AAAAGwwAAAwMAAAmOAAAFOnEXhXEYh3EZUnEaWA0AAABzZXNzaW9u
X25vdGVzcRtoBVgOAAAAc2V0X2JyZWFrcG9pbnRxHIlYBwAAAHZlcmJvc2VxHYl1Lg==
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
            "node6",
            "outdata",
            "node7",
            "data"
        ],
        [
            "node7",
            "data",
            "node9",
            "data"
        ],
        [
            "node4",
            "data",
            "node5",
            "data"
        ],
        [
            "node4",
            "data",
            "node20",
            "data"
        ],
        [
            "node3",
            "data",
            "node12",
            "data"
        ],
        [
            "node13",
            "data",
            "node14",
            "data"
        ],
        [
            "node5",
            "data",
            "node6",
            "data2"
        ],
        [
            "node5",
            "data",
            "node10",
            "data"
        ],
        [
            "node5",
            "data",
            "node16",
            "data"
        ],
        [
            "node5",
            "data",
            "node40",
            "data"
        ],
        [
            "node2",
            "data",
            "node18",
            "data"
        ],
        [
            "node2",
            "data",
            "node21",
            "data"
        ],
        [
            "node18",
            "data",
            "node3",
            "data"
        ],
        [
            "node18",
            "data",
            "node17",
            "data"
        ],
        [
            "node18",
            "data",
            "node6",
            "data1"
        ],
        [
            "node18",
            "data",
            "node8",
            "data"
        ],
        [
            "node18",
            "data",
            "node22",
            "data1"
        ],
        [
            "node18",
            "data",
            "node39",
            "data1"
        ],
        [
            "node1",
            "data",
            "node19",
            "data"
        ],
        [
            "node16",
            "data",
            "node22",
            "data2"
        ],
        [
            "node22",
            "outdata",
            "node23",
            "data"
        ],
        [
            "node23",
            "data",
            "node24",
            "data"
        ],
        [
            "node28",
            "data",
            "node26",
            "data"
        ],
        [
            "node27",
            "outdata",
            "node28",
            "data"
        ],
        [
            "node25",
            "data",
            "node27",
            "data2"
        ],
        [
            "node29",
            "data",
            "node9",
            "output_root"
        ],
        [
            "node29",
            "data",
            "node24",
            "output_root"
        ],
        [
            "node29",
            "data",
            "node26",
            "output_root"
        ],
        [
            "node29",
            "data",
            "node8",
            "output_root"
        ],
        [
            "node29",
            "data",
            "node21",
            "output_root"
        ],
        [
            "node29",
            "data",
            "node10",
            "output_root"
        ],
        [
            "node29",
            "data",
            "node20",
            "output_root"
        ],
        [
            "node29",
            "data",
            "node34",
            "output_root"
        ],
        [
            "node29",
            "data",
            "node38",
            "output_root"
        ],
        [
            "node29",
            "data",
            "node42",
            "output_root"
        ],
        [
            "node30",
            "data",
            "node28",
            "srate"
        ],
        [
            "node30",
            "data",
            "node23",
            "srate"
        ],
        [
            "node30",
            "data",
            "node7",
            "srate"
        ],
        [
            "node30",
            "data",
            "node33",
            "srate"
        ],
        [
            "node30",
            "data",
            "node37",
            "srate"
        ],
        [
            "node30",
            "data",
            "node41",
            "srate"
        ],
        [
            "node31",
            "data",
            "node32",
            "data2"
        ],
        [
            "node32",
            "outdata",
            "node33",
            "data"
        ],
        [
            "node33",
            "data",
            "node34",
            "data"
        ],
        [
            "node35",
            "data",
            "node36",
            "data2"
        ],
        [
            "node36",
            "outdata",
            "node37",
            "data"
        ],
        [
            "node37",
            "data",
            "node38",
            "data"
        ],
        [
            "node39",
            "outdata",
            "node41",
            "data"
        ],
        [
            "node41",
            "data",
            "node42",
            "data"
        ],
        [
            "node40",
            "data",
            "node39",
            "data2"
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
            "uuid": "886993b3-e015-4cee-be3f-036a6b4290a9"
        },
        "node10": {
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
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
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
            "uuid": "e0c01721-0024-4226-844b-564ff9843e25"
        },
        "node11": {
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
            "uuid": "51392aec-1652-4ebe-b384-16a77b98a477"
        },
        "node12": {
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
            "uuid": "f0f5f56d-3b79-4baf-a2be-0ca5d286fe5a"
        },
        "node13": {
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
            "uuid": "46ce7de0-3a72-47c7-b5a1-b9e2b0266205"
        },
        "node14": {
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
            "uuid": "9f841e53-5560-4703-976d-991b3abb3054"
        },
        "node15": {
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
            "uuid": "d1fd5f8c-63f6-4e88-8afd-1a5c725b0dbf"
        },
        "node16": {
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
                    "value": -0.02141
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
            "uuid": "5746b58a-399f-495a-b074-d0060939248b"
        },
        "node17": {
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
            "uuid": "94b88594-9dee-4b00-9a24-154b768f5c35"
        },
        "node18": {
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
            "uuid": "d75d5a04-133e-471a-aa47-219d253698c4"
        },
        "node19": {
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
            "uuid": "b6aa18da-01b7-42d2-8b6a-8e027811d5a6"
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
            "uuid": "1beb457e-99dd-48ac-8370-32a544c63ef7"
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
                    "value": "raw-eeg.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
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
            "uuid": "ce751895-4521-4096-97ee-40985a8e3dc1"
        },
        "node21": {
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
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
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
            "uuid": "0f0a4146-943d-4c8a-bd65-b53886515dc6"
        },
        "node22": {
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
            "uuid": "c21ecbc4-97f5-4515-ac94-718feeee98ac"
        },
        "node23": {
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
                    "value": 120
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
            "uuid": "b1335326-a3cd-44d4-b796-7a928a60da83"
        },
        "node24": {
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
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
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
            "uuid": "d0730f37-fbb1-44c6-b61b-0e32aa4acdb5"
        },
        "node25": {
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
                        24
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
            "uuid": "1421bf9d-8441-4ed3-aa4a-100fdac90420"
        },
        "node26": {
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
                    "value": "dejittered-iir-4order-1to24-eeg-and-dejittered-eyetracking.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
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
            "uuid": "ed48b790-0d7f-4e15-b93f-dd6fcec2faf3"
        },
        "node27": {
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
            "uuid": "572c6f4f-07c8-4d3b-9203-9ffa379a3740"
        },
        "node28": {
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
                    "value": 120
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
            "uuid": "549af808-3ef8-4c54-8e61-dced199d1eca"
        },
        "node29": {
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
                    "value": "C:/Users/vizlab_stud/idatt2900_gr92/neuropype-pipeline/LSLData"
                }
            },
            "uuid": "9c554161-6a56-428e-a717-ee04700c4a66"
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
            "uuid": "34e7b9bb-28fc-4b28-a040-851390f1360a"
        },
        "node30": {
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
                    "value": 120
                }
            },
            "uuid": "cd244cfd-4a23-4d8f-bd6a-c68ddace1dc2"
        },
        "node31": {
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
                        24
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
                    "value": 3
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
            "uuid": "f609a2aa-35e8-4a33-a201-6ca4c9fe5460"
        },
        "node32": {
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
            "uuid": "21713dd6-bd0f-4472-b743-903e87fffb67"
        },
        "node33": {
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
                    "customized": false,
                    "type": "IntPort",
                    "value": 125
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
            "uuid": "27744b40-1ce0-4266-beac-0d1e40fc2d65"
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
                    "value": "dejittered-iir-3order-1to24-eeg-and-dejittered-eyetracking.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
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
            "uuid": "a0c781c6-2ba6-4fbf-9f2f-4d62e4abce2b"
        },
        "node35": {
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
                        0.75,
                        5
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
            "uuid": "011a6fae-08d1-4662-97a3-3ab51f77ee4a"
        },
        "node36": {
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
            "uuid": "6c7c9a74-3484-40e2-a15b-acff44bbb4ef"
        },
        "node37": {
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
                    "customized": false,
                    "type": "IntPort",
                    "value": 125
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
            "uuid": "5d2b8892-5e36-40ad-bf6f-11ee18a19d6d"
        },
        "node38": {
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
                    "value": "dejittered-iir-4order-0.75to5-eeg-and-dejittered-eyetracking.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
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
            "uuid": "64d77bf7-a24e-421f-a567-9211df0f0f67"
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
            "uuid": "bb0d8df2-b91a-4df1-b68e-492e17373025"
        },
        "node4": {
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
            "uuid": "23a0f320-33ae-4ffe-92cd-fb350ad17042"
        },
        "node40": {
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
                        0.75,
                        5
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
                    "value": 3
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
            "uuid": "d42a8fbe-489e-4dd5-8663-05d60176a628"
        },
        "node41": {
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
                    "customized": false,
                    "type": "IntPort",
                    "value": 125
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
            "uuid": "af385ce8-10ca-493e-8790-d0a69b4a708d"
        },
        "node42": {
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
                    "value": "dejittered-iir-3order-0.75to5-eeg-and-dejittered-eyetracking.xdf"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
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
            "uuid": "eefb1dae-e803-4b7f-b2f6-c97a3952f932"
        },
        "node5": {
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
            "uuid": "573dacb6-b1c8-4fca-a4c7-a861cf5d2678"
        },
        "node6": {
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
            "uuid": "153cd31d-628e-47e3-8561-0b1cbb896d89"
        },
        "node7": {
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
            "uuid": "c01f5f3c-1f04-44b3-80d4-70d1114f3233"
        },
        "node8": {
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
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
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
            "uuid": "1947116c-f8a3-4f3c-a4f2-31957f7c0537"
        },
        "node9": {
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
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
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
            "uuid": "a5af9fa4-9315-4098-a74e-9b41add6be63"
        }
    },
    "version": 1.1
}</patch>
</scheme>
