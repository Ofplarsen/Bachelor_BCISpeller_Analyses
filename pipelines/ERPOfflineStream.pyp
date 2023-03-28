<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="test" version="2.0">
	<nodes>
		<node id="0" name="Import File" position="(312.0, 312.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportfile.OWImportFile" title="Import File" uuid="77298836-e6ab-4d42-815e-f0a928910ff0" version="1.2.1" />
		<node id="1" name="Stream Data" position="(508.0, 322.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="a14c4057-de66-4fda-86ea-d0379ba20fcd" version="1.2.1" />
		<node id="2" name="LSL Output" position="(667.0, 324.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="75070f23-8e0e-4cbb-88dc-db3ab4a05b29" version="1.4.3" />
		<node id="3" name="Inspect Data" position="(623.0, 197.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectdata.OWInspectData" title="Inspect Data" uuid="41bdc55f-b466-481d-b6d0-d9690bd06c96" version="2.2.4" />
		<node id="4" name="LSL Input" position="(315.0, 451.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="b278cd57-b627-4a30-b34c-3cca5d9664cf" version="1.3.6" />
		<node id="5" name="Inspect Data" position="(494.0, 442.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectdata.OWInspectData" title="Inspect Data (1)" uuid="9a97fa23-fece-4e61-bf84-bc00eb95122c" version="2.2.4" />
		<node id="6" name="LSL Output" position="(671.0, 617.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="696da7f8-1cc3-4036-986e-43c3cb17cbdc" version="1.4.3" />
		<node id="7" name="Stream Data" position="(511.0, 615.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="e0ad4490-5a6a-4456-917f-ba2be97fcc6b" version="1.2.1" />
		<node id="8" name="Import File" position="(320.0, 605.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportfile.OWImportFile" title="Import File" uuid="67330d7e-eb99-48ea-857c-f164df968783" version="1.2.1" />
		<node id="9" name="Record to CSV" position="(464.0, 550.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtocsv.OWRecordToCSV" title="Record to CSV" uuid="40ede1ba-0e58-47c1-baaa-616a5db57234" version="1.0.1" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="8" />
		<link enabled="false" id="6" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="8" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWBgAAABhbGxvd19pbnNlY3VyZV9maWxldHlwZXNxAYlYDQAAAGNsb3VkX2FjY291bnRx
AlgAAAAAcQNYDAAAAGNsb3VkX2J1Y2tldHEEaANYEQAAAGNsb3VkX2NyZWRlbnRpYWxzcQVoA1gK
AAAAY2xvdWRfaG9zdHEGWAcAAABEZWZhdWx0cQdYCAAAAGZpbGVuYW1lcQhYegAAAEM6L1VzZXJz
L3hyYXkyL09uZURyaXZlL0RvY3VtZW50cy9OVE5VL0RhdGFJbmcyMDIzL3MyMDIzL2JhL25ldXJv
cHlwZS1waXBlbGluZS9qaXR0ZXIvZGF0YS9CQ0lTcGVsbGVyVjYvZGVqaXR0ZXJlZC1lZWcueGRm
cQlYCwAAAGxvYWRfZXZlbnRzcQqIWAwAAABsb2FkX3NpZ25hbHNxC4hYCAAAAG1ldGFkYXRhcQx9
cQ1YDgAAAHJldGFpbl9zdHJlYW1zcQ5YDQAAACh1c2UgZGVmYXVsdClxD1gTAAAAc2F2ZWRXaWRn
ZXRHZW9tZXRyeXEQY3NpcApfdW5waWNrbGVfdHlwZQpxEVgMAAAAUHlRdDUuUXRDb3JlcRJYCgAA
AFFCeXRlQXJyYXlxE0NCAdnQywADAAAAAAMLAAABOgAABHQAAAMPAAADDAAAAVkAAARzAAADDgAA
AAAAAAAAB4AAAAMMAAABWQAABHMAAAMOcRSFcRWHcRZScRdYCAAAAHNlZ21lbnRzcRhoD1gOAAAA
c2V0X2JyZWFrcG9pbnRxGYlYEAAAAHNpZ25hbF9hdXRvc2NhbGVxGohYDAAAAHN0aW1fY2hhbm5l
bHEbaANYCwAAAHRpbWVfYm91bmRzcRxoD1gPAAAAdXNlX3N0cmVhbW5hbWVzcR2JdS4=
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWAoAAABkYXRhX2R0eXBlcQFYBwAAAGZsb2F0NjRxAlgRAAAAaGl0Y2hfcHJvYmFiaWxp
dHlxA0cAAAAAAAAAAFgOAAAAaml0dGVyX3BlcmNlbnRxBEsFWAwAAABsb2dfcHJvZ3Jlc3NxBYlY
BwAAAGxvb3BpbmdxBohYCAAAAG1ldGFkYXRhcQd9cQhYCAAAAHJhbmRzZWVkcQlN54ZYEwAAAHNh
dmVkV2lkZ2V0R2VvbWV0cnlxCmNzaXAKX3VucGlja2xlX3R5cGUKcQtYDAAAAFB5UXQ1LlF0Q29y
ZXEMWAoAAABRQnl0ZUFycmF5cQ1DQgHZ0MsAAwAAAAADCwAAAS4AAAR0AAACxAAAAwwAAAFNAAAE
cwAAAsMAAAAAAAAAAAeAAAADDAAAAU0AAARzAAACw3EOhXEPh3EQUnERWA4AAABzZXRfYnJlYWtw
b2ludHESiVgHAAAAc3BlZWR1cHETRz/wAAAAAAAAWAkAAABzdGFydF9wb3NxFEcAAAAAAAAAAFgQ
AAAAdGltZXN0YW1wX2ppdHRlcnEVRwAAAAAAAAAAWAYAAAB0aW1pbmdxFlgJAAAAd2FsbGNsb2Nr
cRdYDwAAAHVwZGF0ZV9pbnRlcnZhbHEYRz+keuFHrhR7dS4=
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYEwAA
AGtlZXBfc2luZ2xldG9uX2F4ZXNxA4lYDAAAAG1hcmtlcl9maWVsZHEEWAYAAABNYXJrZXJxBVgL
AAAAbWFya2VyX25hbWVxBlgRAAAAT3V0U3RyZWFtLW1hcmtlcnNxB1gQAAAAbWFya2VyX3NvdXJj
ZV9pZHEIWAAAAABxCVgMAAAAbWF4X2J1ZmZlcmVkcQpLPFgIAAAAbWV0YWRhdGFxC31xDFgXAAAA
bnVtZXJpY19sYWJlbF9wcmVjaXNpb25xDUsBWBgAAABudW1lcmljX21hcmtlcl9wcmVjaXNpb25x
DksDWBcAAAByZXNldF9pZl9sYWJlbHNfY2hhbmdlZHEPiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEQY3NpcApfdW5waWNrbGVfdHlwZQpxEVgMAAAAUHlRdDUuUXRDb3JlcRJYCgAAAFFCeXRlQXJy
YXlxE0NCAdnQywADAAAAAAMLAAABAgAABHQAAAM0AAADDAAAASEAAARzAAADMwAAAAAAAAAAB4AA
AAMMAAABIQAABHMAAAMzcRSFcRWHcRZScRdYDAAAAHNlbmRfbWFya2Vyc3EYiVgJAAAAc2VwYXJh
dG9ycRlYAQAAAC1xGlgOAAAAc2V0X2JyZWFrcG9pbnRxG4lYCQAAAHNvdXJjZV9pZHEcaAlYBQAA
AHNyYXRlcR1YDQAAACh1c2UgZGVmYXVsdClxHlgLAAAAc3RyZWFtX25hbWVxH1gVAAAATGl2ZUFt
cFNOLTA1NjMwOS0wNTMzcSBYCwAAAHN0cmVhbV90eXBlcSFYAwAAAEVFR3EiWBMAAAB1c2VfZGF0
YV90aW1lc3RhbXBzcSOIWBYAAAB1c2VfbnVtcHlfb3B0aW1pemF0aW9ucSSJdS4=
</properties>
		<properties format="literal" node_id="3">{'always_on_top': True, 'auto_close': True, 'col_axis': 'time', 'decimals': 6, 'every_n_ticks': 1, 'fewer_buttons': False, 'font_size': 10, 'initial_position': [20, 50, 500, 400], 'metadata': {}, 'row_axis': 'space', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'show_axes_table': True, 'show_data_table': True, 'show_markers_table': True, 'show_max_columns': 20, 'show_max_values': 50, 'show_streams_table': True, 'stream_name': '(use default)', 'window_title': 'Inspect Data Packet'}</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWAwAAABt
YXJrZXJfcXVlcnlxCFgAAAAAcQlYDAAAAG1heF9ibG9ja2xlbnEKTQAEWAoAAABtYXhfYnVmbGVu
cQtLHlgMAAAAbWF4X2NodW5rbGVucQxLAFgIAAAAbWV0YWRhdGFxDX1xDlgMAAAAbm9taW5hbF9y
YXRlcQ9YDQAAACh1c2UgZGVmYXVsdClxEFgJAAAAb21pdF9kZXNjcRGJWA8AAABwcmVhbGxvY19i
dWZmZXJxEohYDgAAAHByb2NfY2xvY2tzeW5jcROIWA0AAABwcm9jX2Rlaml0dGVycRSJWA8AAABw
cm9jX21vbm90b25pemVxFYlYDwAAAHByb2NfdGhyZWFkc2FmZXEWiVgFAAAAcXVlcnlxF1gKAAAA
bmFtZT0nQ0NBJ3EYWAcAAAByZWNvdmVycRmIWBQAAAByZXNvbHZlX21pbmltdW1fdGltZXEaRz/g
AAAAAAAAWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRtjc2lwCl91bnBpY2tsZV90eXBlCnEcWAwA
AABQeVF0NS5RdENvcmVxHVgKAAAAUUJ5dGVBcnJheXEeQ0IB2dDLAAMAAAAAAwwAAAF3AAAEcwAA
ApkAAAMMAAABdwAABHMAAAKZAAAAAAAAAAAHgAAAAwwAAAF3AAAEcwAAAplxH4VxIIdxIVJxIlgO
AAAAc2V0X2JyZWFrcG9pbnRxI4l1Lg==
</properties>
		<properties format="literal" node_id="5">{'always_on_top': True, 'auto_close': True, 'col_axis': 'time', 'decimals': 6, 'every_n_ticks': 1, 'fewer_buttons': False, 'font_size': 10, 'initial_position': [20, 50, 500, 400], 'metadata': {}, 'row_axis': 'space', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'show_axes_table': True, 'show_data_table': True, 'show_markers_table': True, 'show_max_columns': 20, 'show_max_values': 50, 'show_streams_table': True, 'stream_name': '(use default)', 'window_title': 'Inspect Data Packet'}</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYEwAA
AGtlZXBfc2luZ2xldG9uX2F4ZXNxA4lYDAAAAG1hcmtlcl9maWVsZHEEWAYAAABNYXJrZXJxBVgL
AAAAbWFya2VyX25hbWVxBlgRAAAAT3V0U3RyZWFtLW1hcmtlcnNxB1gQAAAAbWFya2VyX3NvdXJj
ZV9pZHEIWAAAAABxCVgMAAAAbWF4X2J1ZmZlcmVkcQpLPFgIAAAAbWV0YWRhdGFxC31xDFgXAAAA
bnVtZXJpY19sYWJlbF9wcmVjaXNpb25xDUsBWBgAAABudW1lcmljX21hcmtlcl9wcmVjaXNpb25x
DksDWBcAAAByZXNldF9pZl9sYWJlbHNfY2hhbmdlZHEPiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEQY3NpcApfdW5waWNrbGVfdHlwZQpxEVgMAAAAUHlRdDUuUXRDb3JlcRJYCgAAAFFCeXRlQXJy
YXlxE0NCAdnQywADAAAAAAMLAAAA4AAABHQAAAMSAAADDAAAAP8AAARzAAADEQAAAAAAAAAAB4AA
AAMMAAAA/wAABHMAAAMRcRSFcRWHcRZScRdYDAAAAHNlbmRfbWFya2Vyc3EYiVgJAAAAc2VwYXJh
dG9ycRlYAQAAAC1xGlgOAAAAc2V0X2JyZWFrcG9pbnRxG4lYCQAAAHNvdXJjZV9pZHEcaAlYBQAA
AHNyYXRlcR1YDQAAACh1c2UgZGVmYXVsdClxHlgLAAAAc3RyZWFtX25hbWVxH1gSAAAAU2FtcGxl
UG9pbnRDb3VudGVycSBYCwAAAHN0cmVhbV90eXBlcSFYAQAAAE5xIlgTAAAAdXNlX2RhdGFfdGlt
ZXN0YW1wc3EjiFgWAAAAdXNlX251bXB5X29wdGltaXphdGlvbnEkiXUu
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWAoAAABkYXRhX2R0eXBlcQFYBwAAAGZsb2F0NjRxAlgRAAAAaGl0Y2hfcHJvYmFiaWxp
dHlxA0cAAAAAAAAAAFgOAAAAaml0dGVyX3BlcmNlbnRxBEsFWAwAAABsb2dfcHJvZ3Jlc3NxBYlY
BwAAAGxvb3BpbmdxBohYCAAAAG1ldGFkYXRhcQd9cQhYCAAAAHJhbmRzZWVkcQlN54ZYEwAAAHNh
dmVkV2lkZ2V0R2VvbWV0cnlxCmNzaXAKX3VucGlja2xlX3R5cGUKcQtYDAAAAFB5UXQ1LlF0Q29y
ZXEMWAoAAABRQnl0ZUFycmF5cQ1DQgHZ0MsAAwAAAAADCwAAAS4AAAR0AAACxAAAAwwAAAFNAAAE
cwAAAsMAAAAAAAAAAAeAAAADDAAAAU0AAARzAAACw3EOhXEPh3EQUnERWA4AAABzZXRfYnJlYWtw
b2ludHESiVgHAAAAc3BlZWR1cHETRz/wAAAAAAAAWAkAAABzdGFydF9wb3NxFEcAAAAAAAAAAFgQ
AAAAdGltZXN0YW1wX2ppdHRlcnEVRwAAAAAAAAAAWAYAAAB0aW1pbmdxFlgJAAAAd2FsbGNsb2Nr
cRdYDwAAAHVwZGF0ZV9pbnRlcnZhbHEYRz+keuFHrhR7dS4=
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWBgAAABhbGxvd19pbnNlY3VyZV9maWxldHlwZXNxAYlYDQAAAGNsb3VkX2FjY291bnRx
AlgAAAAAcQNYDAAAAGNsb3VkX2J1Y2tldHEEaANYEQAAAGNsb3VkX2NyZWRlbnRpYWxzcQVoA1gK
AAAAY2xvdWRfaG9zdHEGWAcAAABEZWZhdWx0cQdYCAAAAGZpbGVuYW1lcQhYkAAAAEM6L1VzZXJz
L3hyYXkyL09uZURyaXZlL0RvY3VtZW50cy9OVE5VL0RhdGFJbmcyMDIzL3MyMDIzL2JhL25ldXJv
cHlwZS1waXBlbGluZS9qaXR0ZXIvZGF0YS9CQ0lTcGVsbGVyVjYvZGVqaXR0ZXJlZC11bml0eS1m
cmVxdWVuY2llcy1ZZm9ybWF0LnhkZnEJWAsAAABsb2FkX2V2ZW50c3EKiFgMAAAAbG9hZF9zaWdu
YWxzcQuIWAgAAABtZXRhZGF0YXEMfXENWA4AAAByZXRhaW5fc3RyZWFtc3EOWA0AAAAodXNlIGRl
ZmF1bHQpcQ9YEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEGNzaXAKX3VucGlja2xlX3R5cGUKcRFY
DAAAAFB5UXQ1LlF0Q29yZXESWAoAAABRQnl0ZUFycmF5cRNDQgHZ0MsAAwAAAAADCwAAAQ4AAAR0
AAAC4wAAAwwAAAEtAAAEcwAAAuIAAAAAAAAAAAeAAAADDAAAAS0AAARzAAAC4nEUhXEVh3EWUnEX
WAgAAABzZWdtZW50c3EYWA0AAAAodXNlIGRlZmF1bHQpcRlYDgAAAHNldF9icmVha3BvaW50cRqJ
WBAAAABzaWduYWxfYXV0b3NjYWxlcRuIWAwAAABzdGltX2NoYW5uZWxxHGgDWAsAAAB0aW1lX2Jv
dW5kc3EdWA0AAAAodXNlIGRlZmF1bHQpcR5YDwAAAHVzZV9zdHJlYW1uYW1lc3EfiXUu
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWBcAAABhYnNvbHV0ZV9pbnN0YW5jZV90aW1lc3EBiFgNAAAAY2xvdWRfYWNjb3VudHEC
WAAAAABxA1gMAAAAY2xvdWRfYnVja2V0cQRoA1gRAAAAY2xvdWRfY3JlZGVudGlhbHNxBWgDWAoA
AABjbG91ZF9ob3N0cQZYBwAAAERlZmF1bHRxB1gNAAAAY29sdW1uX2hlYWRlcnEIiFgMAAAAZGVs
ZXRlX3BhcnRzcQmIWAgAAABmaWxlbmFtZXEKWAgAAAB0ZXN0LmNzdnELWAgAAABtZXRhZGF0YXEM
fXENWAsAAABvdXRwdXRfcm9vdHEOWFgAAABDOi9Vc2Vycy94cmF5Mi9PbmVEcml2ZS9Eb2N1bWVu
dHMvTlROVS9EYXRhSW5nMjAyMy9zMjAyMy9iYS9uZXVyb3B5cGUtcGlwZWxpbmUvcGlwZWxpbmVz
cQ9YCwAAAHJldHJpZXZhYmxlcRCJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRFjc2lwCl91bnBp
Y2tsZV90eXBlCnESWAwAAABQeVF0NS5RdENvcmVxE1gKAAAAUUJ5dGVBcnJheXEUQ0IB2dDLAAMA
AAAAAwsAAAEmAAAEdAAAAssAAAMMAAABRQAABHMAAALKAAAAAAAAAAAHgAAAAwwAAAFFAAAEcwAA
AspxFYVxFodxF1JxGFgOAAAAc2V0X2JyZWFrcG9pbnRxGYlYCwAAAHRpbWVfc3RhbXBzcRqIWA8A
AAB0aW1lc3RhbXBfbGFiZWxxG1gJAAAAdGltZXN0YW1wcRx1Lg==
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
            "node1",
            "data",
            "node2",
            "data"
        ],
        [
            "node2",
            "data",
            "node3",
            "data"
        ],
        [
            "node2",
            "data",
            "node4",
            "data"
        ],
        [
            "node5",
            "data",
            "node6",
            "data"
        ],
        [
            "node8",
            "data",
            "node7",
            "data"
        ],
        [
            "node9",
            "data",
            "node8",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "ImportFile",
            "module": "neuropype.nodes.file_system.ImportFile",
            "params": {
                "allow_insecure_filetypes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
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
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/xray2/OneDrive/Documents/NTNU/DataIng2023/s2023/ba/neuropype-pipeline/jitter/data/BCISpellerV6/dejittered-eeg.xdf"
                },
                "load_events": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "load_signals": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "segments": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "signal_autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "stim_channel": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "time_bounds": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "77298836-e6ab-4d42-815e-f0a928910ff0"
        },
        "node10": {
            "class": "RecordToCSV",
            "module": "neuropype.nodes.file_system.RecordToCSV",
            "params": {
                "absolute_instance_times": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
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
                "column_header": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "test.csv"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/xray2/OneDrive/Documents/NTNU/DataIng2023/s2023/ba/neuropype-pipeline/pipelines"
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_stamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "timestamp_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "timestamp"
                }
            },
            "uuid": "40ede1ba-0e58-47c1-baaa-616a5db57234"
        },
        "node2": {
            "class": "StreamData",
            "module": "neuropype.nodes.formatting.StreamData",
            "params": {
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "hitch_probability": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "jitter_percent": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "log_progress": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "looping": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "randseed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 34535
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "speedup": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "start_pos": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timestamp_jitter": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timing": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "wallclock"
                },
                "update_interval": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.04
                }
            },
            "uuid": "a14c4057-de66-4fda-86ea-d0379ba20fcd"
        },
        "node3": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "keep_singleton_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "marker_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "numeric_label_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "numeric_marker_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 3
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "separator": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "-"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "LiveAmpSN-056309-0533"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "EEG"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "75070f23-8e0e-4cbb-88dc-db3ab4a05b29"
        },
        "node4": {
            "class": "InspectData",
            "module": "neuropype.nodes.visualization.InspectData",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_close": {
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
                    "value": true
                },
                "show_max_columns": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 20
                },
                "show_max_values": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 0
                },
                "show_streams_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "eeg"
                },
                "window_title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Inspect Data Packet"
                }
            },
            "uuid": "41bdc55f-b466-481d-b6d0-d9690bd06c96"
        },
        "node5": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "Unknown1"
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
                    "value": "name='CCA'"
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
                }
            },
            "uuid": "b278cd57-b627-4a30-b34c-3cca5d9664cf"
        },
        "node6": {
            "class": "InspectData",
            "module": "neuropype.nodes.visualization.InspectData",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_close": {
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
                    "value": true
                },
                "show_max_columns": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 20
                },
                "show_max_values": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 0
                },
                "show_streams_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "cca"
                },
                "window_title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Inspect Data Packet"
                }
            },
            "uuid": "9a97fa23-fece-4e61-bf84-bc00eb95122c"
        },
        "node7": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "keep_singleton_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "marker_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "numeric_label_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "numeric_marker_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 3
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "separator": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "-"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "SamplePointCounter"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "N"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "696da7f8-1cc3-4036-986e-43c3cb17cbdc"
        },
        "node8": {
            "class": "StreamData",
            "module": "neuropype.nodes.formatting.StreamData",
            "params": {
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "hitch_probability": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "jitter_percent": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "log_progress": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "looping": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "randseed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 34535
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "speedup": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "start_pos": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timestamp_jitter": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timing": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "wallclock"
                },
                "update_interval": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.04
                }
            },
            "uuid": "e0ad4490-5a6a-4456-917f-ba2be97fcc6b"
        },
        "node9": {
            "class": "ImportFile",
            "module": "neuropype.nodes.file_system.ImportFile",
            "params": {
                "allow_insecure_filetypes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
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
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/xray2/OneDrive/Documents/NTNU/DataIng2023/s2023/ba/neuropype-pipeline/jitter/data/BCISpellerV6/dejittered-unity-frequencies-Yformat.xdf"
                },
                "load_events": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "load_signals": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "segments": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "signal_autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "stim_channel": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "time_bounds": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "67330d7e-eb99-48ea-857c-f164df968783"
        }
    },
    "version": 1.1
}</patch>
</scheme>
