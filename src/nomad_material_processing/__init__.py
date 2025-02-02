#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import (
    TYPE_CHECKING,
)
import numpy as np
from nomad.metainfo import (
    Package,
    Quantity,
    Section,
    SubSection,
    Datetime,
    MEnum,
)
from nomad.datamodel.metainfo.basesections import (
    ElementalComposition,
    SynthesisMethod,
    CompositeSystem,
    CompositeSystemReference,
    SystemComponent,
)
from nomad.datamodel.data import (
    ArchiveSection,
)
from nomad.datamodel.metainfo.annotations import (
    ELNAnnotation,
    ELNComponentEnum,
)
from nomad.datamodel.metainfo.workflow import (
    Link,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )


m_package = Package(name='Material Processing')


class Geometry(ArchiveSection):
    """
    Geometrical shape attributes of a system.
    Sections derived from `Geometry` represent concrete geometrical shapes.
    """

    m_def = Section()
    volume = Quantity(
        type=float,
        description='The measure of the amount of space occupied in 3D space.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
        ),
        unit='meter ** 3',
    )


class Parallelepiped(Geometry):
    """
    Six-faced polyhedron with each pair of opposite faces parallel and equal in size,
    characterized by rectangular sides and parallelogram faces.
    """

    m_def = Section()
    height = Quantity(
        type=float,
        description='The z dimension of the parallelepiped.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='millimeter',
            label='Height (z)',
        ),
        unit='meter',
    )
    width = Quantity(
        type=float,
        description='The x dimension of the parallelepiped.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='millimeter',
            label='Width (x)',
        ),
        unit='meter',
    )
    length = Quantity(
        type=float,
        description='The y dimension of the parallelepiped.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='millimeter',
            label='Length (y)',
        ),
        unit='meter',
    )
    alpha = Quantity(
        type=float,
        description='The angle between y and z sides.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            label='Alpha (∡ y-x-z)',
        ),
        unit='degree',
    )
    beta = Quantity(
        type=float,
        description='The angle between x and z sides.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            label='Beta (∡ x-y-z)',
        ),
        unit='degree',
    )
    gamma = Quantity(
        type=float,
        description='The angle between x and y sides.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            label='Gamma (∡ x-z-y)',
        ),
        unit='degree',
    )
    surface_area = Quantity(
        type=float,
        description="""
        The product of length and width, representing the total exposed area of the
        primary surface.
        """,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='millimeter ** 2',
            label='Surface Area (x*y)',
        ),
        unit='meter ** 2',
    )


class SquareCuboid(Parallelepiped):
    """
    A cuboid with all sides equal in length.
    """
    m_def = Section()
    height = Quantity(
        type=float,
        description='The z dimension of the parallelepiped.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='millimeter',
            label='Height (z)',
        ),
        unit='meter',
    )
    side = Quantity(
        type=float,
        description='The x and y dimensions of the parallelepiped.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='millimeter',
            label='Side (x = y)',
        ),
        unit='meter',
    )
    surface_area = Quantity(
        type=float,
        description="""
        The product of length and width, representing the total exposed area of the
        primary surface.
        """,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='millimeter ** 2',
            label='Surface Area (x*y)',
        ),
        unit='meter ** 2',
    )


class RectangleCuboid(Parallelepiped):
    """
    A rectangular cuboid is a specific type of parallelepiped
    where all angles between adjacent faces are right angles,
    and all faces are rectangles.
    """
    m_def = Section()
    height = Quantity(
        type=float,
        description='The z dimension of the parallelepiped.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='millimeter',
            label='Height (z)',
        ),
        unit='meter',
    )
    width = Quantity(
        type=float,
        description='The x dimension of the parallelepiped.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='millimeter',
            label='Width (x)',
        ),
        unit='meter',
    )
    length = Quantity(
        type=float,
        description='The y dimension of the parallelepiped.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='millimeter',
            label='Length (y)',
        ),
        unit='meter',
    )
    surface_area = Quantity(
        type=float,
        description="""
        The product of length and width, representing the total exposed area of the
        primary surface.
        """,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='millimeter ** 2',
            label='Surface Area (x*y)',
        ),
        unit='meter ** 2',
    )


class TruncatedCone(Geometry):
    """
    A cone with the top cut off parallel to the cone bottom.
    """

    m_def = Section()
    height = Quantity(
        type=float,
        description='The z dimension of the parallelepiped.',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
            defaultDisplayUnit='nanometer',
        ),
        label='Height (z)',
        unit='meter',
    )
    lower_cap_radius = Quantity(
        type=float,
        description='Radius of the lower cap.',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
            defaultDisplayUnit='millimeter',
        ),
        unit='meter',
    )
    upper_cap_radius = Quantity(
        type=float,
        description='Radius of the upper cap.',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
            defaultDisplayUnit='millimeter',
        ),
        unit='meter',
    )
    lower_cap_surface_area = Quantity(
        type=float,
        description='Area of the lower cap.',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
            defaultDisplayUnit='millimeter ** 2',
        ),
        unit='meter ** 2',
    )
    upper_cap_surface_area = Quantity(
        type=float,
        description='Area of the upper cap.',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
            defaultDisplayUnit='millimeter ** 2',
        ),
        unit='meter ** 2',
    )
    lateral_surface_area = Quantity(
        type=float,
        description='Area of the lateral surface.',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
            defaultDisplayUnit='millimeter ** 2',
        ),
        unit='meter ** 2',
    )


class Cylinder(Geometry):
    """
    A cylinder, i.e. a prism with a circular base.
    """

    m_def = Section()
    height = Quantity(
        type=float,
        description='The z dimension of the parallelepiped.',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
            defaultDisplayUnit='nanometer',
        ),
        label='Height (z)',
        unit='meter',
    )
    radius = Quantity(
        type=float,
        description='Radius of the cylinder.',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
            defaultDisplayUnit='millimeter',
        ),
        unit='meter',
    )
    lower_cap_surface_area = Quantity(
        type=float,
        description='Area of the lower cap.',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
            defaultDisplayUnit='millimeter ** 2',
        ),
        unit='meter ** 2',
    )
    cap_surface_area = Quantity(
        type=float,
        description='Area of the cap.',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
            defaultDisplayUnit='millimeter ** 2',
        ),
        unit='meter ** 2',
    )
    lateral_surface_area = Quantity(
        type=float,
        description='Area of the lateral surface.',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
            defaultDisplayUnit='millimeter ** 2',
        ),
        unit='meter ** 2',
    )


class CylinderSector(Cylinder):
    central_angle = Quantity(
        type=float,
        description="""The angle that defines the portion of the cylinder.
        This angle is taken at the center of the base circle
        and extends to the arc that defines the cylindrical sector.""",
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
        ),
        unit='degree',
    )


class IrregularParallelSurfaces(Geometry):
    """
    A shape that does not fit into any of the other geometry classes.
    """

    m_def = Section()
    height = Quantity(
        type=float,
        description='The z dimension of the irregular shape.',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
            defaultDisplayUnit='nanometer',
        ),
        label='Height (z)',
        unit='meter',
    )


class Miscut(ArchiveSection):
    """
    The miscut in a crystalline substrate refers to
    the intentional deviation from a specific crystallographic orientation,
    commonly expressed as the angular displacement of a crystal plane.
    """

    angle = Quantity(
        type=float,
        description="""
        The angular displacement from the crystallographic orientation of the substrate.
        """,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='deg',
            label='Miscut Angle',
        ),
        unit='deg',
    )
    angle_deviation = Quantity(
        type=float,
        description='The ± deviation in the angular displacement.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='deg',
            label='± Miscut Angle Deviation',
        ),
        unit='deg',
    )
    orientation = Quantity(
        type=str,
        description='The direction of the miscut in Miller index, [hkl].',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity,
            label='Miscut Orientation [hkl]',
        ),
    )


class Dopant(ElementalComposition):
    """
    A dopant element in a crystalline structure
    is a foreign atom intentionally introduced into the crystal lattice.
    """

    doping_level = Quantity(
        type=float,
        description='The chemical doping level.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='1 / cm ** 3',
        ),
        unit='1 / m ** 3',
    )
    doping_deviation = Quantity(
        type=float,
        description='The ± deviation in the doping level.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='1 / cm ** 3',
        ),
        unit='1 / m ** 3',
    )


class CrystalProperties(ArchiveSection):
    """
    Characteristics arising from the ordered arrangement of atoms in a crystalline structure.
    These properties are defined by factors such as crystal symmetry, lattice parameters,
    and the specific arrangement of atoms within the crystal lattice.
    """


class SubstrateCrystalProperties(CrystalProperties):
    """
    Crystallographic parameters such as orientation, miscut, and surface structure.
    """
    bravais_lattices = Quantity(
        type=MEnum(
            'Triclinic',
            'Monoclinic Simple',
            'Monoclinic Base Centered',
            'Orthorhombic Simple',
            'Orthorhombic Base Centered',
            'Orthorhombic Body Centered',
            'Orthorhombic Face Centered',
            'Tetragonal Simple',
            'Tetragonal Body Centered',
            'Cubic Simple',
            'Cubic Body Centered',
            'Cubic Face Centered',
            'Trigonal',
            'Hexagonal',
        ),
        description='The crystal system of the substrate.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.EnumEditQuantity,
        ),
    )
    orientation = Quantity(
        type=str,
        description="""
        Alignment of crystal lattice with respect to a vector normal to the surface
        specified using Miller indices.
        """,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity,
            label='Substrate Orientation (hkl)',
        ),
    )
    miscut = SubSection(
        section_def=Miscut,
        description="""
        Section describing any miscut of the substrate with respect to the substrate
        orientation.
        """,
        repeats=True,
    )


class ElectronicProperties(ArchiveSection):
    """
    The electronic properties of a material.
    """

    m_def = Section()

    conductivity_type = Quantity(
        type=MEnum(
            'P-type',
            'N-type',
        ),
        description='The type of semiconductor, N-type being electrons the majority carriers and P-type being holes the majority carriers.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.EnumEditQuantity,
        ),
    )
    carrier_density = Quantity(
        type=np.dtype(float),
        unit='1 / cm**3',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
        ),
        description='Concentration of free charge carriers, electrons in the conduction band and holes in the valence band.',
    )
    electrical_resistivity = Quantity(
        type=float,
        links=['http://fairmat-nfdi.eu/taxonomy/ElectricalResistivity'],
        description='Resistance of the charges to move in the presence of an electric current.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='ohm cm',
        ),
        unit='ohm m',
    )


class Substrate(CompositeSystem):
    """
    A thin free standing sheet of material. Not to be confused with the substrate role
    during a deposition, which can be a `Substrate` with `ThinFilm`(s) on it.
    """

    m_def = Section()

    supplier = Quantity(
        type=str,
        description='The supplier of the current substrate specimen.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity,
        ),
    )
    supplier_id = Quantity(
        type=str,
        description='An ID string that is unique from the supplier.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity,
            label='Supplier ID',
        ),
    )
    lab_id = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity,
            label='Substrate ID',
        ),
    )
    image = Quantity(
        type=str,
        description='A photograph or image of the substrate.',
        a_browser={'adaptor': 'RawFileAdaptor'},
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.FileEditQuantity,
        ),
    )
    information_sheet = Quantity(
        type=str,
        description='Pdf files containing certificate and other documentation.',
        a_browser={'adaptor': 'RawFileAdaptor'},
        a_eln=ELNAnnotation(
            component='FileEditQuantity',
        ),
    )


class CrystallineSubstrate(Substrate):
    """
    The substrate defined in this class is composed of periodic arrangement of atoms
    and shows typical features of a crystal structure.
    """

    m_def = Section()


    geometry = SubSection(
        section_def=Geometry,
        description='Section containing the geometry of the substrate.',
    )
    crystal_properties = SubSection(
        section_def=SubstrateCrystalProperties,
        description='Section containing the crystal properties of the substrate.',
    )
    electronic_properties = SubSection(
        section_def=ElectronicProperties,
        description='Section containing the electronic properties of the substrate.',
    )
    dopants = SubSection(
        section_def=Dopant,
        repeats=True,
        description="""
        Repeating section containing information on any dopants in the substrate.
        """,
    )


class ThinFilm(CompositeSystem):
    """
    A thin film of material which exists as part of a stack.
    """

    m_def = Section()

    geometry = SubSection(
        section_def=Geometry,
        description='Section containing the geometry of the thin film.',
    )


class ThinFilmReference(CompositeSystemReference):
    """
    Class autogenerated from yaml schema.
    """

    lab_id = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity,
            label='Thin Film ID',
        ),
    )
    reference = Quantity(
        type=ThinFilm,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.ReferenceEditQuantity,
            label='Thin Film',
        ),
    )


class SubstrateReference(CompositeSystemReference):
    """
    A section for describing a system component and its role in a composite system.
    """

    lab_id = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity,
            label='Substrate ID',
        ),
    )
    reference = Quantity(
        type=Substrate,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.ReferenceEditQuantity,
            label='Substrate',
        ),
    )


class ThinFilmStack(CompositeSystem):
    """
    A stack of `ThinFilm`(s). Typically deposited on a `Substrate`.
    """

    m_def = Section(
        a_eln=ELNAnnotation(
            hide=[
                'components',
            ],
        ),
    )
    layers = SubSection(
        description="""
        An ordered list (starting at the substrate) of the thin films making up the
        thin film stacks.
        """,
        section_def=ThinFilmReference,
        repeats=True,
    )
    substrate = SubSection(
        description="""
        The substrate which the thin film layers of the thin film stack are deposited
        on.
        """,
        section_def=SubstrateReference,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `ThinFilmStack` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        self.components = []
        if self.layers:
            self.components = [
                SystemComponent(system=layer.reference)
                for layer in self.layers
                if layer.reference
            ]
        if self.substrate.reference:
            self.components.append(SystemComponent(system=self.substrate.reference))
        super().normalize(archive, logger)


class ThinFilmStackReference(CompositeSystemReference):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    lab_id = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.StringEditQuantity,
        ),
    )
    reference = Quantity(
        type=ThinFilmStack,
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.ReferenceEditQuantity,
        ),
    )


class SampleDeposition(SynthesisMethod):
    """
    The process of the settling of particles (atoms or molecules) from a solution,
    suspension or vapour onto a pre-existing surface, resulting in the growth of a
    new phase. [database_cross_reference: https://orcid.org/0000-0002-0640-0422]

    Synonyms:
     - deposition
    """

    m_def = Section(
        links=['http://purl.obolibrary.org/obo/CHMO_0001310'],
    )

    def is_serial(self) -> bool:
        """
        Method for determining if the steps are serial. Can be overwritten by sub class.
        Default behavior is to return True if all steps start after the previous one.

        Returns:
            bool: Whether or not the steps are serial.
        """
        start_times = []
        durations = []
        for step in self.steps:
            if step.start_time is None or step.duration is None:
                return False
            start_times.append(step.start_time.timestamp())
            durations.append(step.duration.to('s').magnitude)
        start_times = np.array(start_times)
        durations = np.array(durations)
        end_times = start_times + durations
        diffs = start_times[1:] - end_times[:-1]
        if np.any(diffs < 0):
            return False
        return True

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `SampleDeposition` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)
        if self.is_serial():
            tasks = []
            previous = None
            for step in self.steps:
                task = step.to_task()
                task.outputs.append(Link(name=step.name, section=step))
                if previous is not None:
                    task.inputs.append(Link(name=previous.name, section=previous))
                tasks.append(task)
                previous = step
            archive.workflow2.tasks = tasks


class TimeSeries(ArchiveSection):
    """
    A time series of data during a process step.
    This is an abstract class and should not be used directly.
    Instead, it should be derived and the the units of the `value` and `set_value` should
    be specified.

    For example, a derived class could be `Temperature` with `value` in Kelvin:
    ```python
    class Temperature(TimeSeries):
        value = TimeSeries.value.m_copy()
        value.unit = "kelvin"
        set_value = TimeSeries.set_value.m_copy()
        set_value.unit = "kelvin"
        set_value.a_eln.defaultDisplayUnit = "celsius"
    ```
    """

    m_def = Section(
        a_plot=dict(
            # x=['time', 'set_time'],
            # y=['value', 'set_value'],
            x='time',
            y='value',
        ),
    )
    set_value = Quantity(
        type=float,
        description='The set value(s) (i.e. the intended values) set.',
        shape=['*'],
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            label='Set value',
        ),
    )
    set_time = Quantity(
        type=float,
        unit='s',
        description="""
        The process time when each of the set values were set.
        If this is empty and only one set value is present, it is assumed that the value
        was set at the start of the process step.
        If two set values are present, it is assumed that a linear ramp between the two
        values was set.
        """,
        shape=['*'],
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.NumberEditQuantity,
            defaultDisplayUnit='s',
            label='Set time',
        ),
    )
    value = Quantity(
        type=float,
        description='The observed value as a function of time.',
        shape=['*'],
    )
    time = Quantity(
        type=float,
        unit='s',
        description='The process time when each of the values were recorded.',
        shape=['*'],
    )


m_package.__init_metainfo__()
