<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="EEGAndEyeTracker" version="2.0">
	<nodes>
		<node id="0" name="LSL Input" position="(1512.0, 799.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="ObjectPositionStream" uuid="fe171ff7-79af-4d35-988c-76cf08aaa5a7" version="1.5.1" />
		<node id="1" name="LSL Input" position="(-5.0, 153.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="EyeTrackerStream" uuid="bb14af00-0e54-486b-a8df-f21cc494686a" version="1.5.1" />
		<node id="2" name="Select Range" position="(395.0, 253.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Blinking Data" uuid="59de2da0-8c3f-4860-9b76-9394194adff5" version="1.1.0" />
		<node id="3" name="LSL Input" position="(-9.0, 1311.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="EEG" uuid="21d82681-5001-4dc9-b75f-cde8cbc07967" version="1.5.1" />
		<node id="4" name="Time Series Plot" position="(944.0, 1407.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot" uuid="6490c461-84c5-48bc-8dba-4c1e29ae15fb" version="1.1.0" />
		<node id="5" name="Dejitter Timestamps" position="(161.0, 1321.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="e4d2491c-96e2-4649-8266-2bc9d62bdd55" version="1.0.0" />
		<node id="6" name="FIR Filter" position="(261.0, 1521.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="63f2e294-b2c7-4ff7-a237-0eb566e65673" version="1.1.0" />
		<node id="7" name="Remove Unlocalized Channels" position="(461.0, 1421.0)" project_name="NeuroPype" qualified_name="widgets.source_localization.owremoveunlocalizedchannels.OWRemoveUnlocalizedChannels" title="Remove Unlocalized Channels" uuid="4e41e332-4816-49c7-a5ee-65bc489f9afd" version="1.2.0" />
		<node id="8" name="Bad Channel Removal" position="(583.0, 1554.0)" project_name="NeuroPype" qualified_name="widgets.neural.owbadchannelremoval.OWBadChannelRemoval" title="Bad Channel Removal" uuid="030da87e-19e6-442f-b744-4d473ca547cf" version="1.1.2" />
		<node id="9" name="Artifact Removal" position="(713.0, 1550.0)" project_name="NeuroPype" qualified_name="widgets.neural.owartifactremoval.OWArtifactRemoval" title="Artifact Removal" uuid="746cea4a-2306-45f3-bc23-b38ab96bd9df" version="2.4.1" />
		<node id="10" name="Interpolate Missing Channels" position="(844.0, 1407.0)" project_name="NeuroPype" qualified_name="widgets.neural.owinterpolatemissingchannels.OWInterpolateMissingChannels" title="Interpolate Missing Channels" uuid="473157c6-2dbc-4257-b444-77321c204e79" version="1.4.0" />
		<node id="11" name="Time Series Plot" position="(566.0, 1310.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot (1)" uuid="54a441dd-3a78-412a-b464-9593c20b7627" version="1.1.0" />
		<node id="12" name="Assign Channel Locations" position="(376.0, 1505.0)" project_name="NeuroPype" qualified_name="widgets.source_localization.owassignchannellocations.OWAssignChannelLocations" title="Assign Channel Locations" uuid="29a9d58a-7e0e-48f3-8330-1bdedc504f61" version="1.1.0" />
		<node id="13" name="Extract Channel Names" position="(600.0, 1409.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owextractchannels.OWExtractChannels" title="Extract Channel Names" uuid="0b646755-979e-4dbc-b577-f1661990d14b" version="1.0.1" />
		<node id="14" name="Merge Streams" position="(474.0, 476.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams" uuid="5fb7c373-f818-47d1-bba8-0eef1827364e" version="1.0.0" />
		<node id="15" name="Fuse Streams" position="(642.0, 488.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams" uuid="4f90a6f1-8e76-4eca-9911-3fdac51d5c69" version="0.9.6" />
		<node id="16" name="Record to XDF" position="(122.0, 290.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF" uuid="12b91532-477f-4dab-b804-e48bc1ace34b" version="1.4.0" />
		<node id="17" name="Record to XDF" position="(813.0, 477.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (3)" uuid="331a863a-bbf1-440f-ac14-f249bda321b7" version="1.4.0" />
		<node id="18" name="Record to XDF" position="(129.0, 1454.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (1)" uuid="150d14f1-fabf-4919-b5ab-49ee31f09cea" version="1.4.0" />
		<node id="19" name="Record to XDF" position="(1737.0, 923.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (2)" uuid="71ff55e7-cf47-4b20-a363-50e7d924cb90" version="1.4.0" />
		<node id="20" name="Time Series Plot" position="(623.0, 183.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot (2)" uuid="0be72fa5-c7ae-4d6e-9614-47715f9999fd" version="1.1.0" />
		<node id="21" name="Add Event Marker" position="(926.0, 317.0)" project_name="NeuroPype" qualified_name="widgets.markers.owaddeventmarker.OWAddEventMarker" title="Add Event Marker" uuid="00faadf8-e128-400f-b507-671be6fe7cf2" version="1.1.0" />
		<node id="22" name="Marker Stream Window" position="(1078.0, 324.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owmarkerstreamwindow.OWMarkerStreamWindow" title="Marker Stream Window" uuid="1f0c2725-bf10-4acc-b2ce-ffea690a91bb" version="1.1.1" />
		<node id="23" name="Break Structure" position="(1228.0, 324.0)" project_name="NeuroPype" qualified_name="widgets.programming.owbreakstructure.OWBreakStructure" title="Break Structure" uuid="e7a37855-1299-4e73-b948-f53eef261817" version="1.0.0" />
		<node id="24" name="Shift Timestamps" position="(268.0, 1254.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owshifttimestamps.OWShiftTimestamps" title="Shift Timestamps" uuid="64a655ab-60cf-4a6f-aa48-644280b68115" version="1.2.1" />
		<node id="25" name="Inspect Packet" position="(349.0, 106.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectpacket.OWInspectPacket" title="Inspect Packet" uuid="b1f9c362-6691-4bf0-a260-74b70a2c2575" version="3.0.1" />
		<node id="26" name="Dejitter Timestamps" position="(109.0, 160.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps (2)" uuid="1ffe9cef-2771-4d0b-a29c-130ee1b26780" version="1.0.0" />
		<node id="27" name="Record to XDF" position="(448.0, 1609.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (4)" uuid="69cfd7d9-354e-4a9c-a08b-51485ba19d2a" version="1.4.0" />
		<node id="28" name="Dejitter Timestamps" position="(1650.0, 793.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps (1)" uuid="aefe3d3a-e209-4152-b16f-1fbc5c75f0b3" version="1.0.0" />
		<node id="29" name="Record to XDF" position="(25.0, 1465.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (5)" uuid="1cb78164-8aff-470e-bb2d-13989f86fd05" version="1.4.0" />
		<node id="30" name="Merge Streams" position="(497.0, 696.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams (1)" uuid="553b3366-d59d-4c88-8952-77a38ffbb3d2" version="1.0.0" />
		<node id="31" name="Fuse Streams" position="(621.0, 714.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams (1)" uuid="03d8109e-6a1d-4030-b958-4d50e80f684c" version="0.9.6" />
		<node id="32" name="Record to XDF" position="(779.0, 708.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (6)" uuid="d367af0d-1712-42f2-ac99-1ff08d2abf0a" version="1.4.0" />
		<node id="33" name="Record to XDF" position="(33.0, 286.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (7)" uuid="51bd4c97-5d3a-4fd9-970e-0ac8d0f5ef70" version="1.4.0" />
		<node id="34" name="Merge Streams" position="(500.0, 924.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams (2)" uuid="600f3277-eaa0-4fca-9deb-b54040954469" version="1.0.0" />
		<node id="35" name="Fuse Streams" position="(645.0, 926.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams (2)" uuid="60224fe7-a6ef-4acd-b2cc-8946fab9067e" version="0.9.6" />
		<node id="36" name="Record to XDF" position="(789.0, 929.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (8)" uuid="ebea7845-a231-406f-9b9c-c0e03feeb857" version="1.4.0" />
		<node id="37" name="Shift Timestamps" position="(366.0, 1372.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owshifttimestamps.OWShiftTimestamps" title="Shift Timestamps (1)" uuid="7537d9c6-b9fa-4640-8aa1-504c3aee6428" version="1.2.1" />
		<node id="38" name="Merge Streams" position="(503.0, 1144.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams (3)" uuid="47b121a1-74bc-4498-859c-dbd4bf0f3b34" version="1.0.0" />
		<node id="39" name="Fuse Streams" position="(636.0, 1127.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" title="Fuse Streams (3)" uuid="c98bc806-f938-4490-9be1-96b194fc05e4" version="0.9.6" />
		<node id="40" name="Record to XDF" position="(794.0, 1134.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF (9)" uuid="c1891460-9e6c-4509-93e8-0dd6feef1818" version="1.4.0" />
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
ZXEPS3hYCwAAAHN0cmVhbV9uYW1lcRBYAwAAAGVlZ3ERWAkAAAB2ZXJib3NpdHlxEksBdS4=
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
QXJyYXlxF0NCAdnQywADAAAAAAbDAAADAwAACCoAAAU6AAAGwwAAAwMAAAgqAAAFOgAAAAAAAAAA
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
		<properties format="literal" node_id="31">{'buffer_delay': 2, 'desired_headroom': 5, 'metadata': {}, 'min_headroom': 2, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'srate': 125, 'stream_name': 'eeg', 'verbosity': 1}</properties>
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
		<properties format="literal" node_id="35">{'buffer_delay': 2, 'desired_headroom': 5, 'metadata': {}, 'min_headroom': 2, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'srate': 125, 'stream_name': 'eeg', 'verbosity': 1}</properties>
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
		<properties format="literal" node_id="38">{'metadata': {}, 'replace_if_exists': False, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'sorting': 'input'}</properties>
		<properties format="literal" node_id="39">{'buffer_delay': 2, 'desired_headroom': 5, 'metadata': {}, 'min_headroom': 2, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'srate': 125, 'stream_name': 'eeg', 'verbosity': 1}</properties>
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
            "uuid": "fe171ff7-79af-4d35-988c-76cf08aaa5a7"
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
            "uuid": "746cea4a-2306-45f3-bc23-b38ab96bd9df"
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
                    "customized": false,
                    "type": "ListPort",
                    "value": null
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
            "uuid": "473157c6-2dbc-4257-b444-77321c204e79"
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
            "uuid": "54a441dd-3a78-412a-b464-9593c20b7627"
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
            "uuid": "29a9d58a-7e0e-48f3-8330-1bdedc504f61"
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
            "uuid": "0b646755-979e-4dbc-b577-f1661990d14b"
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
            "uuid": "5fb7c373-f818-47d1-bba8-0eef1827364e"
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
            "uuid": "4f90a6f1-8e76-4eca-9911-3fdac51d5c69"
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
            "uuid": "12b91532-477f-4dab-b804-e48bc1ace34b"
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
            "uuid": "331a863a-bbf1-440f-ac14-f249bda321b7"
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
            "uuid": "150d14f1-fabf-4919-b5ab-49ee31f09cea"
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
            "uuid": "bb14af00-0e54-486b-a8df-f21cc494686a"
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
            "uuid": "71ff55e7-cf47-4b20-a363-50e7d924cb90"
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
            "uuid": "0be72fa5-c7ae-4d6e-9614-47715f9999fd"
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
            "uuid": "00faadf8-e128-400f-b507-671be6fe7cf2"
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
            "uuid": "1f0c2725-bf10-4acc-b2ce-ffea690a91bb"
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
            "uuid": "e7a37855-1299-4e73-b948-f53eef261817"
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
            "uuid": "64a655ab-60cf-4a6f-aa48-644280b68115"
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
            "uuid": "b1f9c362-6691-4bf0-a260-74b70a2c2575"
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
            "uuid": "1ffe9cef-2771-4d0b-a29c-130ee1b26780"
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
            "uuid": "69cfd7d9-354e-4a9c-a08b-51485ba19d2a"
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
            "uuid": "aefe3d3a-e209-4152-b16f-1fbc5c75f0b3"
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
            "uuid": "59de2da0-8c3f-4860-9b76-9394194adff5"
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
            "uuid": "1cb78164-8aff-470e-bb2d-13989f86fd05"
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
            "uuid": "553b3366-d59d-4c88-8952-77a38ffbb3d2"
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
            "uuid": "03d8109e-6a1d-4030-b958-4d50e80f684c"
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
            "uuid": "d367af0d-1712-42f2-ac99-1ff08d2abf0a"
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
            "uuid": "51bd4c97-5d3a-4fd9-970e-0ac8d0f5ef70"
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
            "uuid": "600f3277-eaa0-4fca-9deb-b54040954469"
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
            "uuid": "60224fe7-a6ef-4acd-b2cc-8946fab9067e"
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
            "uuid": "ebea7845-a231-406f-9b9c-c0e03feeb857"
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
            "uuid": "7537d9c6-b9fa-4640-8aa1-504c3aee6428"
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
            "uuid": "47b121a1-74bc-4498-859c-dbd4bf0f3b34"
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
            "uuid": "21d82681-5001-4dc9-b75f-cde8cbc07967"
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
            "uuid": "c98bc806-f938-4490-9be1-96b194fc05e4"
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
            "uuid": "c1891460-9e6c-4509-93e8-0dd6feef1818"
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
            "uuid": "6490c461-84c5-48bc-8dba-4c1e29ae15fb"
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
            "uuid": "e4d2491c-96e2-4649-8266-2bc9d62bdd55"
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
            "uuid": "63f2e294-b2c7-4ff7-a237-0eb566e65673"
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
            "uuid": "4e41e332-4816-49c7-a5ee-65bc489f9afd"
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
            "uuid": "030da87e-19e6-442f-b744-4d473ca547cf"
        }
    },
    "version": 1.1
}</patch>
</scheme>
