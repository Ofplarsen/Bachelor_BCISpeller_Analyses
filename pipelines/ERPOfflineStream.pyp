<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="test" version="2.0">
	<nodes>
		<node id="0" name="Import File" position="(313.0, 312.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportfile.OWImportFile" title="Import File" uuid="c48e3d3b-88c0-4472-a399-856df53bc944" version="1.2.2" />
		<node id="1" name="Stream Data" position="(508.0, 322.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="15c71e45-0a8e-447c-95be-1c45a5845e20" version="1.3.0" />
		<node id="2" name="LSL Output" position="(667.0, 324.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="3df7d0e0-492e-40f2-b110-6e5b478e5ff6" version="1.4.3" />
		<node id="3" name="Inspect Data" position="(623.0, 197.0)" project_name="NeuroPype" qualified_name="widgets.deprecated.owinspectdata.OWInspectData" title="Inspect Data" uuid="608af224-229f-45f1-8b2e-9641dfeba3c7" version="1.0.0" />
		<node id="4" name="LSL Input" position="(315.0, 451.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="f67706f9-ea5d-4b1b-96a9-9251feb3056d" version="1.5.1" />
		<node id="5" name="Inspect Data" position="(494.0, 442.0)" project_name="NeuroPype" qualified_name="widgets.deprecated.owinspectdata.OWInspectData" title="Inspect Data (1)" uuid="43497e3b-6d02-4ea8-850b-7ea2c9f3fed4" version="1.0.0" />
		<node id="6" name="LSL Output" position="(671.0, 617.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="dcc2e553-74ac-4771-ae65-8a0798b380be" version="1.4.3" />
		<node id="7" name="Stream Data" position="(511.0, 615.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="a976adc0-c429-4c14-9d93-278594b15fcd" version="1.3.0" />
		<node id="8" name="Import File" position="(320.0, 605.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportfile.OWImportFile" title="Import File" uuid="203c5319-2f06-4a05-86a5-db9644ef0bf3" version="1.2.2" />
		<node id="9" name="Record to CSV" position="(464.0, 550.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtocsv.OWRecordToCSV" title="Record to CSV" uuid="2e256199-337a-4e1b-a93a-073a0f7ea5d3" version="1.0.1" />
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
AAAAY2xvdWRfaG9zdHEGWAcAAABEZWZhdWx0cQdYCAAAAGZpbGVuYW1lcQhYbwAAAEM6L1VzZXJz
L3ZpemxhYl9zdHVkL2lkYXR0MjkwMF9ncjkyL25ldXJvcHlwZS1waXBlbGluZS9CQ0lTcGVsbGVy
U2NyZWVuVjEvQkNJU3BlbGxlclNjcmVlbl9BL2Rlaml0dGVyZWQtZWVnLnhkZnEJWAsAAABsb2Fk
X2V2ZW50c3EKiFgMAAAAbG9hZF9zaWduYWxzcQuIWAgAAABtZXRhZGF0YXEMfXENWA4AAAByZXRh
aW5fc3RyZWFtc3EOWA0AAAAodXNlIGRlZmF1bHQpcQ9YEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlx
EGNzaXAKX3VucGlja2xlX3R5cGUKcRFYDAAAAFB5UXQ1LlF0Q29yZXESWAoAAABRQnl0ZUFycmF5
cRNDQgHZ0MsAAwAAAAADjgAAAnMAAAvGAAAE2AAAA48AAAKgAAALxQAABNcAAAAAAAAAAA8AAAAD
jwAAAqAAAAvFAAAE13EUhXEVh3EWUnEXWAgAAABzZWdtZW50c3EYaA9YDgAAAHNldF9icmVha3Bv
aW50cRmJWBAAAABzaWduYWxfYXV0b3NjYWxlcRqIWAwAAABzdGltX2NoYW5uZWxxG2gDWAsAAAB0
aW1lX2JvdW5kc3EcaA9YDwAAAHVzZV9zdHJlYW1uYW1lc3EdiXUu
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWAoAAABkYXRhX2R0eXBlcQFYBwAAAGZsb2F0NjRxAlgUAAAAZGF0YV9yYW5nZV90b19z
dHJlYW1xA1gLAAAAbGVnYWN5LXdhcm5xBFgRAAAAaGl0Y2hfcHJvYmFiaWxpdHlxBUcAAAAAAAAA
AFgOAAAAaml0dGVyX3BlcmNlbnRxBksFWAwAAABsb2dfcHJvZ3Jlc3NxB4lYBwAAAGxvb3Bpbmdx
CIhYCAAAAG1ldGFkYXRhcQl9cQpYCAAAAHJhbmRzZWVkcQtN54ZYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxDGNzaXAKX3VucGlja2xlX3R5cGUKcQ1YDAAAAFB5UXQ1LlF0Q29yZXEOWAoAAABRQnl0
ZUFycmF5cQ9DQgHZ0MsAAwAAAAAGfQAAAvIAAAhwAAAFIAAABn4AAAMfAAAIbwAABR8AAAAAAAAA
AA8AAAAGfgAAAx8AAAhvAAAFH3EQhXERh3ESUnETWA4AAABzZXRfYnJlYWtwb2ludHEUiVgHAAAA
c3BlZWR1cHEVRz/wAAAAAAAAWAkAAABzdGFydF9wb3NxFkcAAAAAAAAAAFgQAAAAdGltZXN0YW1w
X2ppdHRlcnEXRwAAAAAAAAAAWAYAAAB0aW1pbmdxGFgJAAAAd2FsbGNsb2NrcRlYDwAAAHVwZGF0
ZV9pbnRlcnZhbHEaRz+keuFHrhR7dS4=
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYEwAA
AGtlZXBfc2luZ2xldG9uX2F4ZXNxA4lYDAAAAG1hcmtlcl9maWVsZHEEWAYAAABNYXJrZXJxBVgL
AAAAbWFya2VyX25hbWVxBlgRAAAAT3V0U3RyZWFtLW1hcmtlcnNxB1gQAAAAbWFya2VyX3NvdXJj
ZV9pZHEIWAAAAABxCVgMAAAAbWF4X2J1ZmZlcmVkcQpLPFgIAAAAbWV0YWRhdGFxC31xDFgXAAAA
bnVtZXJpY19sYWJlbF9wcmVjaXNpb25xDUsBWBgAAABudW1lcmljX21hcmtlcl9wcmVjaXNpb25x
DksDWBcAAAByZXNldF9pZl9sYWJlbHNfY2hhbmdlZHEPiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEQY3NpcApfdW5waWNrbGVfdHlwZQpxEVgMAAAAUHlRdDUuUXRDb3JlcRJYCgAAAFFCeXRlQXJy
YXlxE0NCAdnQywADAAAAAAazAAAClwAACDoAAAV6AAAGtAAAAsQAAAg5AAAFeQAAAAAAAAAADwAA
AAa0AAACxAAACDkAAAV5cRSFcRWHcRZScRdYDAAAAHNlbmRfbWFya2Vyc3EYiVgJAAAAc2VwYXJh
dG9ycRlYAQAAAC1xGlgOAAAAc2V0X2JyZWFrcG9pbnRxG4lYCQAAAHNvdXJjZV9pZHEcaAlYBQAA
AHNyYXRlcR1YDQAAACh1c2UgZGVmYXVsdClxHlgLAAAAc3RyZWFtX25hbWVxH1gVAAAATGl2ZUFt
cFNOLTA1NjMwOS0wNTMzcSBYCwAAAHN0cmVhbV90eXBlcSFYAwAAAEVFR3EiWBMAAAB1c2VfZGF0
YV90aW1lc3RhbXBzcSOIWBYAAAB1c2VfbnVtcHlfb3B0aW1pemF0aW9ucSSJdS4=
</properties>
		<properties format="literal" node_id="3">{'always_on_top': True, 'col_axis': 'time', 'decimals': 6, 'every_n_ticks': 1, 'fewer_buttons': False, 'font_size': 10, 'initial_position': [20, 50, 500, 400], 'metadata': {}, 'row_axis': 'space', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'show_axes_table': True, 'show_data_table': True, 'show_markers_table': True, 'show_max_columns': 20, 'show_max_values': 50, 'show_streams_table': True, 'stream_name': '(use default)', 'verbose': True, 'window_title': 'Inspect Data Packet'}</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWA4AAABs
b2NhbGhvc3Rfb25seXEIiVgMAAAAbWFya2VyX3F1ZXJ5cQlYAAAAAHEKWAwAAABtYXhfYmxvY2ts
ZW5xC00ABFgKAAAAbWF4X2J1ZmxlbnEMSx5YDAAAAG1heF9jaHVua2xlbnENSwBYCAAAAG1ldGFk
YXRhcQ59cQ9YDAAAAG5vbWluYWxfcmF0ZXEQWA0AAAAodXNlIGRlZmF1bHQpcRFYCQAAAG9taXRf
ZGVzY3ESiVgPAAAAcHJlYWxsb2NfYnVmZmVycROIWA4AAABwcm9jX2Nsb2Nrc3luY3EUiFgNAAAA
cHJvY19kZWppdHRlcnEViVgPAAAAcHJvY19tb25vdG9uaXplcRaJWA8AAABwcm9jX3RocmVhZHNh
ZmVxF4lYBQAAAHF1ZXJ5cRhYCgAAAG5hbWU9J0NDQSdxGVgHAAAAcmVjb3ZlcnEaiFgUAAAAcmVz
b2x2ZV9taW5pbXVtX3RpbWVxG0c/4AAAAAAAAFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEcY3Np
cApfdW5waWNrbGVfdHlwZQpxHVgMAAAAUHlRdDUuUXRDb3JlcR5YCgAAAFFCeXRlQXJyYXlxH0NC
AdnQywADAAAAAAMMAAABdwAABHMAAAKZAAADDAAAAXcAAARzAAACmQAAAAAAAAAAB4AAAAMMAAAB
dwAABHMAAAKZcSCFcSGHcSJScSNYDgAAAHNldF9icmVha3BvaW50cSSJWA8AAAB1c2Vfc3RyZWFt
bmFtZXNxJYl1Lg==
</properties>
		<properties format="literal" node_id="5">{'always_on_top': True, 'col_axis': 'time', 'decimals': 6, 'every_n_ticks': 1, 'fewer_buttons': False, 'font_size': 10, 'initial_position': [20, 50, 500, 400], 'metadata': {}, 'row_axis': 'space', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'show_axes_table': True, 'show_data_table': True, 'show_markers_table': True, 'show_max_columns': 20, 'show_max_values': 50, 'show_streams_table': True, 'stream_name': '(use default)', 'verbose': True, 'window_title': 'Inspect Data Packet'}</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYEwAA
AGtlZXBfc2luZ2xldG9uX2F4ZXNxA4lYDAAAAG1hcmtlcl9maWVsZHEEWAYAAABNYXJrZXJxBVgL
AAAAbWFya2VyX25hbWVxBlgRAAAAT3V0U3RyZWFtLW1hcmtlcnNxB1gQAAAAbWFya2VyX3NvdXJj
ZV9pZHEIWAAAAABxCVgMAAAAbWF4X2J1ZmZlcmVkcQpLPFgIAAAAbWV0YWRhdGFxC31xDFgXAAAA
bnVtZXJpY19sYWJlbF9wcmVjaXNpb25xDUsBWBgAAABudW1lcmljX21hcmtlcl9wcmVjaXNpb25x
DksDWBcAAAByZXNldF9pZl9sYWJlbHNfY2hhbmdlZHEPiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEQY3NpcApfdW5waWNrbGVfdHlwZQpxEVgMAAAAUHlRdDUuUXRDb3JlcRJYCgAAAFFCeXRlQXJy
YXlxE0NCAdnQywADAAAAAAazAAAClwAACDoAAAV6AAAGtAAAAsQAAAg5AAAFeQAAAAAAAAAADwAA
AAa0AAACxAAACDkAAAV5cRSFcRWHcRZScRdYDAAAAHNlbmRfbWFya2Vyc3EYiVgJAAAAc2VwYXJh
dG9ycRlYAQAAAC1xGlgOAAAAc2V0X2JyZWFrcG9pbnRxG4lYCQAAAHNvdXJjZV9pZHEcaAlYBQAA
AHNyYXRlcR1YDQAAACh1c2UgZGVmYXVsdClxHlgLAAAAc3RyZWFtX25hbWVxH1gSAAAAU2FtcGxl
UG9pbnRDb3VudGVycSBYCwAAAHN0cmVhbV90eXBlcSFYAQAAAE5xIlgTAAAAdXNlX2RhdGFfdGlt
ZXN0YW1wc3EjiFgWAAAAdXNlX251bXB5X29wdGltaXphdGlvbnEkiXUu
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWAoAAABkYXRhX2R0eXBlcQFYBwAAAGZsb2F0NjRxAlgUAAAAZGF0YV9yYW5nZV90b19z
dHJlYW1xA1gLAAAAbGVnYWN5LXdhcm5xBFgRAAAAaGl0Y2hfcHJvYmFiaWxpdHlxBUcAAAAAAAAA
AFgOAAAAaml0dGVyX3BlcmNlbnRxBksFWAwAAABsb2dfcHJvZ3Jlc3NxB4lYBwAAAGxvb3Bpbmdx
CIhYCAAAAG1ldGFkYXRhcQl9cQpYCAAAAHJhbmRzZWVkcQtN54ZYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxDGNzaXAKX3VucGlja2xlX3R5cGUKcQ1YDAAAAFB5UXQ1LlF0Q29yZXEOWAoAAABRQnl0
ZUFycmF5cQ9DQgHZ0MsAAwAAAAAGfQAAAvIAAAhwAAAFIAAABn4AAAMfAAAIbwAABR8AAAAAAAAA
AA8AAAAGfgAAAx8AAAhvAAAFH3EQhXERh3ESUnETWA4AAABzZXRfYnJlYWtwb2ludHEUiVgHAAAA
c3BlZWR1cHEVRz/wAAAAAAAAWAkAAABzdGFydF9wb3NxFkcAAAAAAAAAAFgQAAAAdGltZXN0YW1w
X2ppdHRlcnEXRwAAAAAAAAAAWAYAAAB0aW1pbmdxGFgJAAAAd2FsbGNsb2NrcRlYDwAAAHVwZGF0
ZV9pbnRlcnZhbHEaRz+keuFHrhR7dS4=
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWBgAAABhbGxvd19pbnNlY3VyZV9maWxldHlwZXNxAYlYDQAAAGNsb3VkX2FjY291bnRx
AlgAAAAAcQNYDAAAAGNsb3VkX2J1Y2tldHEEaANYEQAAAGNsb3VkX2NyZWRlbnRpYWxzcQVoA1gK
AAAAY2xvdWRfaG9zdHEGWAcAAABEZWZhdWx0cQdYCAAAAGZpbGVuYW1lcQhYhQAAAEM6L1VzZXJz
L3ZpemxhYl9zdHVkL2lkYXR0MjkwMF9ncjkyL25ldXJvcHlwZS1waXBlbGluZS9CQ0lTcGVsbGVy
U2NyZWVuVjEvQkNJU3BlbGxlclNjcmVlbl9BL2Rlaml0dGVyZWQtdW5pdHktZnJlcXVlbmNpZXMt
WWZvcm1hdC54ZGZxCVgLAAAAbG9hZF9ldmVudHNxCohYDAAAAGxvYWRfc2lnbmFsc3ELiFgIAAAA
bWV0YWRhdGFxDH1xDVgOAAAAcmV0YWluX3N0cmVhbXNxDlgNAAAAKHVzZSBkZWZhdWx0KXEPWBMA
AABzYXZlZFdpZGdldEdlb21ldHJ5cRBjc2lwCl91bnBpY2tsZV90eXBlCnERWAwAAABQeVF0NS5R
dENvcmVxElgKAAAAUUJ5dGVBcnJheXETQ0IB2dDLAAMAAAAABsIAAALWAAAOBgAABTsAAAbDAAAD
AwAADgUAAAU6AAAAAAAAAAAPAAAABsMAAAMDAAAOBQAABTpxFIVxFYdxFlJxF1gIAAAAc2VnbWVu
dHNxGFgNAAAAKHVzZSBkZWZhdWx0KXEZWA4AAABzZXRfYnJlYWtwb2ludHEaiVgQAAAAc2lnbmFs
X2F1dG9zY2FsZXEbiFgMAAAAc3RpbV9jaGFubmVscRxoA1gLAAAAdGltZV9ib3VuZHNxHVgNAAAA
KHVzZSBkZWZhdWx0KXEeWA8AAAB1c2Vfc3RyZWFtbmFtZXNxH4l1Lg==
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
                    "value": "C:/Users/vizlab_stud/idatt2900_gr92/neuropype-pipeline/BCISpellerScreenV1/BCISpellerScreen_A/dejittered-eeg.xdf"
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
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "c48e3d3b-88c0-4472-a399-856df53bc944"
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
            "uuid": "2e256199-337a-4e1b-a93a-073a0f7ea5d3"
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
                "data_range_to_stream": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "legacy-warn"
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
            "uuid": "15c71e45-0a8e-447c-95be-1c45a5845e20"
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
            "uuid": "3df7d0e0-492e-40f2-b110-6e5b478e5ff6"
        },
        "node4": {
            "class": "InspectData",
            "module": "neuropype.nodes.deprecated.InspectData",
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
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "show_data_table": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
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
                    "customized": true,
                    "type": "IntPort",
                    "value": 0
                },
                "show_streams_table": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "eeg"
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
            "uuid": "608af224-229f-45f1-8b2e-9641dfeba3c7"
        },
        "node5": {
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
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "f67706f9-ea5d-4b1b-96a9-9251feb3056d"
        },
        "node6": {
            "class": "InspectData",
            "module": "neuropype.nodes.deprecated.InspectData",
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
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
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
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
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
            "uuid": "43497e3b-6d02-4ea8-850b-7ea2c9f3fed4"
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
            "uuid": "dcc2e553-74ac-4771-ae65-8a0798b380be"
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
                "data_range_to_stream": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "legacy-warn"
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
            "uuid": "a976adc0-c429-4c14-9d93-278594b15fcd"
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
                    "value": "C:/Users/vizlab_stud/idatt2900_gr92/neuropype-pipeline/BCISpellerScreenV1/BCISpellerScreen_A/dejittered-unity-frequencies-Yformat.xdf"
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
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "203c5319-2f06-4a05-86a5-db9644ef0bf3"
        }
    },
    "version": 1.1
}</patch>
</scheme>
