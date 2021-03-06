#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nova.objects.fields import Architecture


DOMCAPABILITIES_SPARC = """
<domainCapabilities>
  <path>/usr/bin/qemu-system-sparc</path>
  <domain>qemu</domain>
  <machine>SS-5</machine>
  <arch>sparc</arch>
  <vcpu max='1'/>
  <os supported='yes'>
    <loader supported='yes'>
      <enum name='type'>
        <value>rom</value>
        <value>pflash</value>
      </enum>
      <enum name='readonly'>
        <value>yes</value>
        <value>no</value>
      </enum>
    </loader>
  </os>
  <cpu>
    <mode name='host-passthrough' supported='no'/>
    <mode name='host-model' supported='no'/>
    <mode name='custom' supported='no'/>
  </cpu>
  <devices>
    <disk supported='yes'>
      <enum name='diskDevice'>
        <value>disk</value>
        <value>cdrom</value>
        <value>floppy</value>
        <value>lun</value>
      </enum>
      <enum name='bus'>
        <value>fdc</value>
        <value>scsi</value>
        <value>virtio</value>
      </enum>
    </disk>
    <graphics supported='yes'>
      <enum name='type'>
        <value>sdl</value>
        <value>vnc</value>
        <value>spice</value>
      </enum>
    </graphics>
    <video supported='yes'>
      <enum name='modelType'/>
    </video>
    <hostdev supported='yes'>
      <enum name='mode'>
        <value>subsystem</value>
      </enum>
      <enum name='startupPolicy'>
        <value>default</value>
        <value>mandatory</value>
        <value>requisite</value>
        <value>optional</value>
      </enum>
      <enum name='subsysType'>
        <value>usb</value>
        <value>pci</value>
        <value>scsi</value>
      </enum>
      <enum name='capsType'/>
      <enum name='pciBackend'/>
    </hostdev>
  </devices>
  <features>
    <gic supported='no'/>
  </features>
</domainCapabilities>
"""

DOMCAPABILITIES_ARMV7L = """
<domainCapabilities>
  <path>/usr/bin/qemu-system-arm</path>
  <domain>qemu</domain>
  <machine>virt-2.11</machine>
  <arch>armv7l</arch>
  <vcpu max='255'/>
  <os supported='yes'>
    <loader supported='yes'>
      <enum name='type'>
        <value>rom</value>
        <value>pflash</value>
      </enum>
      <enum name='readonly'>
        <value>yes</value>
        <value>no</value>
      </enum>
    </loader>
  </os>
  <cpu>
    <mode name='host-passthrough' supported='no'/>
    <mode name='host-model' supported='no'/>
    <mode name='custom' supported='yes'>
      <model usable='unknown'>pxa262</model>
      <model usable='unknown'>pxa270-a0</model>
      <model usable='unknown'>arm1136</model>
      <model usable='unknown'>cortex-a15</model>
      <model usable='unknown'>pxa260</model>
      <model usable='unknown'>arm1136-r2</model>
      <model usable='unknown'>pxa261</model>
      <model usable='unknown'>pxa255</model>
      <model usable='unknown'>arm926</model>
      <model usable='unknown'>arm11mpcore</model>
      <model usable='unknown'>pxa250</model>
      <model usable='unknown'>ti925t</model>
      <model usable='unknown'>sa1110</model>
      <model usable='unknown'>arm1176</model>
      <model usable='unknown'>sa1100</model>
      <model usable='unknown'>pxa270-c5</model>
      <model usable='unknown'>cortex-a9</model>
      <model usable='unknown'>cortex-a8</model>
      <model usable='unknown'>pxa270-c0</model>
      <model usable='unknown'>cortex-a7</model>
      <model usable='unknown'>arm1026</model>
      <model usable='unknown'>pxa270-b1</model>
      <model usable='unknown'>cortex-m3</model>
      <model usable='unknown'>cortex-m4</model>
      <model usable='unknown'>pxa270-b0</model>
      <model usable='unknown'>arm946</model>
      <model usable='unknown'>cortex-r5</model>
      <model usable='unknown'>pxa270-a1</model>
      <model usable='unknown'>pxa270</model>
    </mode>
  </cpu>
  <devices>
    <disk supported='yes'>
      <enum name='diskDevice'>
        <value>disk</value>
        <value>cdrom</value>
        <value>floppy</value>
        <value>lun</value>
      </enum>
      <enum name='bus'>
        <value>fdc</value>
        <value>scsi</value>
        <value>virtio</value>
        <value>usb</value>
        <value>sata</value>
      </enum>
    </disk>
    <graphics supported='yes'>
      <enum name='type'>
        <value>sdl</value>
        <value>vnc</value>
        <value>spice</value>
      </enum>
    </graphics>
    <video supported='yes'>
      <enum name='modelType'>
        <value>vga</value>
        <value>virtio</value>
      </enum>
    </video>
    <hostdev supported='yes'>
      <enum name='mode'>
        <value>subsystem</value>
      </enum>
      <enum name='startupPolicy'>
        <value>default</value>
        <value>mandatory</value>
        <value>requisite</value>
        <value>optional</value>
      </enum>
      <enum name='subsysType'>
        <value>usb</value>
        <value>pci</value>
        <value>scsi</value>
      </enum>
      <enum name='capsType'/>
      <enum name='pciBackend'/>
    </hostdev>
  </devices>
  <features>
    <gic supported='yes'>
      <enum name='version'>
        <value>2</value>
        <value>3</value>
      </enum>
    </gic>
  </features>
</domainCapabilities>
"""

DOMCAPABILITIES_PPC = """
<domainCapabilities>
  <path>/usr/bin/qemu-system-ppc</path>
  <domain>qemu</domain>
  <machine>g3beige</machine>
  <arch>ppc</arch>
  <vcpu max='1'/>
  <os supported='yes'>
    <loader supported='yes'>
      <enum name='type'>
        <value>rom</value>
        <value>pflash</value>
      </enum>
      <enum name='readonly'>
        <value>yes</value>
        <value>no</value>
      </enum>
    </loader>
  </os>
  <cpu>
    <mode name='host-passthrough' supported='no'/>
    <mode name='host-model' supported='no'/>
    <mode name='custom' supported='no'/>
  </cpu>
  <devices>
    <disk supported='yes'>
      <enum name='diskDevice'>
        <value>disk</value>
        <value>cdrom</value>
        <value>floppy</value>
        <value>lun</value>
      </enum>
      <enum name='bus'>
        <value>ide</value>
        <value>fdc</value>
        <value>scsi</value>
        <value>virtio</value>
        <value>usb</value>
        <value>sata</value>
      </enum>
    </disk>
    <graphics supported='yes'>
      <enum name='type'>
        <value>sdl</value>
        <value>vnc</value>
        <value>spice</value>
      </enum>
    </graphics>
    <video supported='yes'>
      <enum name='modelType'>
        <value>vga</value>
        <value>virtio</value>
      </enum>
    </video>
    <hostdev supported='yes'>
      <enum name='mode'>
        <value>subsystem</value>
      </enum>
      <enum name='startupPolicy'>
        <value>default</value>
        <value>mandatory</value>
        <value>requisite</value>
        <value>optional</value>
      </enum>
      <enum name='subsysType'>
        <value>usb</value>
        <value>pci</value>
        <value>scsi</value>
      </enum>
      <enum name='capsType'/>
      <enum name='pciBackend'/>
    </hostdev>
  </devices>
  <features>
    <gic supported='no'/>
  </features>
</domainCapabilities>
"""

DOMCAPABILITIES_MIPS = """
<domainCapabilities>
  <path>/usr/bin/qemu-system-mips</path>
  <domain>qemu</domain>
  <machine>malta</machine>
  <arch>mips</arch>
  <vcpu max='16'/>
  <os supported='yes'>
    <loader supported='yes'>
      <enum name='type'>
        <value>rom</value>
        <value>pflash</value>
      </enum>
      <enum name='readonly'>
        <value>yes</value>
        <value>no</value>
      </enum>
    </loader>
  </os>
  <cpu>
    <mode name='host-passthrough' supported='no'/>
    <mode name='host-model' supported='no'/>
    <mode name='custom' supported='no'/>
  </cpu>
  <devices>
    <disk supported='yes'>
      <enum name='diskDevice'>
        <value>disk</value>
        <value>cdrom</value>
        <value>floppy</value>
        <value>lun</value>
      </enum>
      <enum name='bus'>
        <value>ide</value>
        <value>fdc</value>
        <value>scsi</value>
        <value>virtio</value>
        <value>usb</value>
        <value>sata</value>
      </enum>
    </disk>
    <graphics supported='yes'>
      <enum name='type'>
        <value>sdl</value>
        <value>vnc</value>
        <value>spice</value>
      </enum>
    </graphics>
    <video supported='yes'>
      <enum name='modelType'>
        <value>vga</value>
        <value>cirrus</value>
        <value>vmvga</value>
        <value>virtio</value>
      </enum>
    </video>
    <hostdev supported='yes'>
      <enum name='mode'>
        <value>subsystem</value>
      </enum>
      <enum name='startupPolicy'>
        <value>default</value>
        <value>mandatory</value>
        <value>requisite</value>
        <value>optional</value>
      </enum>
      <enum name='subsysType'>
        <value>usb</value>
        <value>pci</value>
        <value>scsi</value>
      </enum>
      <enum name='capsType'/>
      <enum name='pciBackend'/>
    </hostdev>
  </devices>
  <features>
    <gic supported='no'/>
  </features>
</domainCapabilities>
"""

DOMCAPABILITIES_MIPSEL = """
<domainCapabilities>
  <path>/usr/bin/qemu-system-mipsel</path>
  <domain>qemu</domain>
  <machine>malta</machine>
  <arch>mipsel</arch>
  <vcpu max='16'/>
  <os supported='yes'>
    <loader supported='yes'>
      <enum name='type'>
        <value>rom</value>
        <value>pflash</value>
      </enum>
      <enum name='readonly'>
        <value>yes</value>
        <value>no</value>
      </enum>
    </loader>
  </os>
  <cpu>
    <mode name='host-passthrough' supported='no'/>
    <mode name='host-model' supported='no'/>
    <mode name='custom' supported='no'/>
  </cpu>
  <devices>
    <disk supported='yes'>
      <enum name='diskDevice'>
        <value>disk</value>
        <value>cdrom</value>
        <value>floppy</value>
        <value>lun</value>
      </enum>
      <enum name='bus'>
        <value>ide</value>
        <value>fdc</value>
        <value>scsi</value>
        <value>virtio</value>
        <value>usb</value>
        <value>sata</value>
      </enum>
    </disk>
    <graphics supported='yes'>
      <enum name='type'>
        <value>sdl</value>
        <value>vnc</value>
        <value>spice</value>
      </enum>
    </graphics>
    <video supported='yes'>
      <enum name='modelType'>
        <value>vga</value>
        <value>cirrus</value>
        <value>vmvga</value>
        <value>virtio</value>
      </enum>
    </video>
    <hostdev supported='yes'>
      <enum name='mode'>
        <value>subsystem</value>
      </enum>
      <enum name='startupPolicy'>
        <value>default</value>
        <value>mandatory</value>
        <value>requisite</value>
        <value>optional</value>
      </enum>
      <enum name='subsysType'>
        <value>usb</value>
        <value>pci</value>
        <value>scsi</value>
      </enum>
      <enum name='capsType'/>
      <enum name='pciBackend'/>
    </hostdev>
  </devices>
  <features>
    <gic supported='no'/>
  </features>
</domainCapabilities>
"""

# NOTE(sean-k-mooney): yes i686 is actually the i386 emulator
# the qemu-system-i386 binary is used for all 32bit x86
# instruction sets.
DOMCAPABILITIES_I686 = """
<domainCapabilities>
  <path>/usr/bin/qemu-system-i386</path>
  <domain>kvm</domain>
  <machine>pc-i440fx-2.11</machine>
  <arch>i686</arch>
  <vcpu max='255'/>
  <os supported='yes'>
    <loader supported='yes'>
      <enum name='type'>
        <value>rom</value>
        <value>pflash</value>
      </enum>
      <enum name='readonly'>
        <value>yes</value>
        <value>no</value>
      </enum>
    </loader>
  </os>
  <cpu>
    <mode name='host-passthrough' supported='yes'/>
    <mode name='host-model' supported='yes'>
      <model fallback='forbid'>Skylake-Client-IBRS</model>
      <vendor>Intel</vendor>
      <feature policy='require' name='ss'/>
      <feature policy='require' name='vmx'/>
      <feature policy='require' name='hypervisor'/>
      <feature policy='require' name='tsc_adjust'/>
      <feature policy='require' name='clflushopt'/>
      <feature policy='require' name='md-clear'/>
      <feature policy='require' name='ssbd'/>
      <feature policy='require' name='xsaves'/>
      <feature policy='require' name='pdpe1gb'/>
    </mode>
    <mode name='custom' supported='yes'>
      <model usable='no'>qemu64</model>
      <model usable='yes'>qemu32</model>
      <model usable='no'>phenom</model>
      <model usable='yes'>pentium3</model>
      <model usable='yes'>pentium2</model>
      <model usable='yes'>pentium</model>
      <model usable='yes'>n270</model>
      <model usable='yes'>kvm64</model>
      <model usable='yes'>kvm32</model>
      <model usable='yes'>coreduo</model>
      <model usable='yes'>core2duo</model>
      <model usable='no'>athlon</model>
      <model usable='yes'>Westmere</model>
      <model usable='yes'>Westmere-IBRS</model>
      <model usable='no'>Skylake-Server</model>
      <model usable='no'>Skylake-Server-IBRS</model>
      <model usable='yes'>Skylake-Client</model>
      <model usable='yes'>Skylake-Client-IBRS</model>
      <model usable='yes'>SandyBridge</model>
      <model usable='yes'>SandyBridge-IBRS</model>
      <model usable='yes'>Penryn</model>
      <model usable='no'>Opteron_G5</model>
      <model usable='no'>Opteron_G4</model>
      <model usable='no'>Opteron_G3</model>
      <model usable='no'>Opteron_G2</model>
      <model usable='yes'>Opteron_G1</model>
      <model usable='yes'>Nehalem</model>
      <model usable='yes'>Nehalem-IBRS</model>
      <model usable='yes'>IvyBridge</model>
      <model usable='yes'>IvyBridge-IBRS</model>
      <model usable='yes'>Haswell-noTSX</model>
      <model usable='yes'>Haswell-noTSX-IBRS</model>
      <model usable='yes'>Haswell</model>
      <model usable='yes'>Haswell-IBRS</model>
      <model usable='no'>EPYC</model>
      <model usable='no'>EPYC-IBPB</model>
      <model usable='yes'>Conroe</model>
      <model usable='yes'>Broadwell-noTSX</model>
      <model usable='yes'>Broadwell-noTSX-IBRS</model>
      <model usable='yes'>Broadwell</model>
      <model usable='yes'>Broadwell-IBRS</model>
      <model usable='yes'>486</model>
    </mode>
  </cpu>
  <devices>
    <disk supported='yes'>
      <enum name='diskDevice'>
        <value>disk</value>
        <value>cdrom</value>
        <value>floppy</value>
        <value>lun</value>
      </enum>
      <enum name='bus'>
        <value>ide</value>
        <value>fdc</value>
        <value>scsi</value>
        <value>virtio</value>
        <value>usb</value>
        <value>sata</value>
      </enum>
    </disk>
    <graphics supported='yes'>
      <enum name='type'>
        <value>sdl</value>
        <value>vnc</value>
        <value>spice</value>
      </enum>
    </graphics>
    <video supported='yes'>
      <enum name='modelType'>
        <value>vga</value>
        <value>cirrus</value>
        <value>vmvga</value>
        <value>qxl</value>
        <value>virtio</value>
      </enum>
    </video>
    <hostdev supported='yes'>
      <enum name='mode'>
        <value>subsystem</value>
      </enum>
      <enum name='startupPolicy'>
        <value>default</value>
        <value>mandatory</value>
        <value>requisite</value>
        <value>optional</value>
      </enum>
      <enum name='subsysType'>
        <value>usb</value>
        <value>pci</value>
        <value>scsi</value>
      </enum>
      <enum name='capsType'/>
      <enum name='pciBackend'/>
    </hostdev>
  </devices>
  <features>
    <gic supported='no'/>
  </features>
</domainCapabilities>
"""

STATIC_DOMCAPABILITIES = {
    Architecture.ARMV7: DOMCAPABILITIES_ARMV7L,
    Architecture.SPARC: DOMCAPABILITIES_SPARC,
    Architecture.PPC: DOMCAPABILITIES_PPC,
    Architecture.MIPS: DOMCAPABILITIES_MIPS,
    Architecture.MIPSEL: DOMCAPABILITIES_MIPSEL,
    Architecture.I686: DOMCAPABILITIES_I686
}

DOMCAPABILITIES_X86_64_TEMPLATE = """
<domainCapabilities>
  <path>/usr/bin/qemu-kvm</path>
  <domain>kvm</domain>
  <machine>%(mtype)s</machine>
  <arch>x86_64</arch>
  <vcpu max='255'/>
  <os supported='yes'>
    <loader supported='yes'>
      <value>/usr/share/qemu/ovmf-x86_64-ms-4m-code.bin</value>
      <value>/usr/share/qemu/ovmf-x86_64-ms-code.bin</value>
      <enum name='type'>
        <value>rom</value>
        <value>pflash</value>
      </enum>
      <enum name='readonly'>
        <value>yes</value>
        <value>no</value>
      </enum>
    </loader>
  </os>
  <cpu>
    <mode name='host-passthrough' supported='yes'/>
    <mode name='host-model' supported='yes'>
      <model fallback='forbid'>EPYC-IBPB</model>
      <vendor>AMD</vendor>
      <feature policy='require' name='x2apic'/>
      <feature policy='require' name='tsc-deadline'/>
      <feature policy='require' name='hypervisor'/>
      <feature policy='require' name='tsc_adjust'/>
      <feature policy='require' name='cmp_legacy'/>
      <feature policy='require' name='invtsc'/>
      <feature policy='require' name='virt-ssbd'/>
      <feature policy='disable' name='monitor'/>
    </mode>
    <mode name='custom' supported='yes'>
      <model usable='yes'>qemu64</model>
      <model usable='yes'>qemu32</model>
      <model usable='no'>phenom</model>
      <model usable='yes'>pentium3</model>
      <model usable='yes'>pentium2</model>
      <model usable='yes'>pentium</model>
      <model usable='no'>n270</model>
      <model usable='yes'>kvm64</model>
      <model usable='yes'>kvm32</model>
      <model usable='no'>coreduo</model>
      <model usable='no'>core2duo</model>
      <model usable='no'>athlon</model>
      <model usable='yes'>Westmere</model>
      <model usable='no'>Westmere-IBRS</model>
      <model usable='no'>Skylake-Server</model>
      <model usable='no'>Skylake-Server-IBRS</model>
      <model usable='no'>Skylake-Client</model>
      <model usable='no'>Skylake-Client-IBRS</model>
      <model usable='yes'>SandyBridge</model>
      <model usable='no'>SandyBridge-IBRS</model>
      <model usable='yes'>Penryn</model>
      <model usable='no'>Opteron_G5</model>
      <model usable='no'>Opteron_G4</model>
      <model usable='yes'>Opteron_G3</model>
      <model usable='yes'>Opteron_G2</model>
      <model usable='yes'>Opteron_G1</model>
      <model usable='yes'>Nehalem</model>
      <model usable='no'>Nehalem-IBRS</model>
      <model usable='no'>IvyBridge</model>
      <model usable='no'>IvyBridge-IBRS</model>
      <model usable='no'>Haswell</model>
      <model usable='no'>Haswell-noTSX</model>
      <model usable='no'>Haswell-noTSX-IBRS</model>
      <model usable='no'>Haswell-IBRS</model>
      <model usable='yes'>EPYC</model>
      <model usable='yes'>EPYC-IBPB</model>
      <model usable='yes'>Conroe</model>
      <model usable='no'>Broadwell</model>
      <model usable='no'>Broadwell-noTSX</model>
      <model usable='no'>Broadwell-noTSX-IBRS</model>
      <model usable='no'>Broadwell-IBRS</model>
      <model usable='yes'>486</model>
    </mode>
  </cpu>
  <devices>
    <disk supported='yes'>
      <enum name='diskDevice'>
        <value>disk</value>
        <value>cdrom</value>
        <value>floppy</value>
        <value>lun</value>
      </enum>
      <enum name='bus'>
        <value>ide</value>
        <value>fdc</value>
        <value>scsi</value>
        <value>virtio</value>
        <value>usb</value>
        <value>sata</value>
      </enum>
    </disk>
    <graphics supported='yes'>
      <enum name='type'>
        <value>sdl</value>
        <value>vnc</value>
        <value>spice</value>
      </enum>
    </graphics>
    <video supported='yes'>
      <enum name='modelType'>
        <value>vga</value>
        <value>cirrus</value>
        <value>vmvga</value>
        <value>qxl</value>
        <value>virtio</value>
      </enum>
    </video>
    <hostdev supported='yes'>
      <enum name='mode'>
        <value>subsystem</value>
      </enum>
      <enum name='startupPolicy'>
        <value>default</value>
        <value>mandatory</value>
        <value>requisite</value>
        <value>optional</value>
      </enum>
      <enum name='subsysType'>
        <value>usb</value>
        <value>pci</value>
        <value>scsi</value>
      </enum>
      <enum name='capsType'/>
      <enum name='pciBackend'>
        <value>default</value>
        <value>vfio</value>
      </enum>
    </hostdev>
  </devices>
%(features)s
</domainCapabilities>
"""
