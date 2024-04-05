'use strict';

/**
 * csi-data service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::csi-data.csi-data');
